#!/usr/bin/python

import json
import urllib2
import httplib
import ssl
from urlparse import urljoin

# compatibility with python 2.7.9+
# see https://www.python.org/dev/peps/pep-0476/
_PYTHON_2_7_9_COMPAT = False
if '_create_unverified_context' in dir(ssl):
    _PYTHON_2_7_9_COMPAT = True


class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
    def __init__(self, key, cert):
        if _PYTHON_2_7_9_COMPAT:
            context = ssl._create_unverified_context()
            urllib2.HTTPSHandler.__init__(self, context=context)
        else:
            urllib2.HTTPSHandler.__init__(self)

        self.key = key
        self.cert = cert

    def https_open(self, req):
        # Rather than pass in a reference to a connection class, we pass in
        # a reference to a function which, for all intents and purposes,
        # will behave as a constructor
        if _PYTHON_2_7_9_COMPAT:
            return self.do_open(self.get_connection, req, context=self._context)
        return self.do_open(self.get_connection, req)

    def get_connection(self, host, context=None, timeout=300):
        if context is not None:
            return httplib.HTTPSConnection(host, key_file=self.key, cert_file=self.cert, context=context)
        return httplib.HTTPSConnection(host, key_file=self.key, cert_file=self.cert)


class API(object):

    class APSExcStruct:
        def __init__(self):
            self.code = 0
            self.type = ''
            self.message = ''

    def __init__(self, url):
        """
        Takes something like the following argument as input:
        url = 'https://a.bvt.aps.sw.ru:6308'
        """
        self.url = url

    def call(self, verb, path, headers=None, data=None, cert=None, rheaders=None):
        data = json.dumps(data)

        # url = self.url + path
        url = urljoin(self.url, path)
        if not headers:
            headers = dict()

        req = urllib2.Request(url, headers=headers, data=data)
        req.get_method = lambda: verb

        resp = None
        try:
            if cert:
                opener = urllib2.build_opener(HTTPSClientAuthHandler(cert, cert))
                resp = opener.open(req)
            else:
                if _PYTHON_2_7_9_COMPAT:
                    context = ssl._create_unverified_context()
                    resp = urllib2.urlopen(req, context=context)
                else:
                    resp = urllib2.urlopen(req)

        except urllib2.HTTPError as error:
            contents = error.read()

            # APS Exceptions have the following structure (example):
            # {
            #    "code": 500,
            #    "type": "APS::Hosting::Exception",
            #    "message": "Limit for resource ..."
            # }
            # In order to allow simple processing of this exception like
            # ('something' in error.aps.message) we convert this exception
            # to JSON directly here.
            error.aps = API.APSExcStruct()
            if len(contents):
                error.aps = json.loads(contents)
            raise error

        if resp.headers:
            if rheaders is not None:
                for h in resp.headers.headers:
                    (k, v) = h.split(':', 1)
                    rheaders[k] = v.strip()

        content = resp.read()

        # Converting JSON immediately if presented
        if len(content):
            content = json.loads(content)

        return content

    def get(self, path, headers=None, data=None, cert=None):
        return self.call('GET', path, headers, data, cert)

    def put(self, path, headers=None, data=None, cert=None):
        return self.call('PUT', path, headers, data, cert)

    def post(self, path, headers=None, data=None, cert=None):
        return self.call('POST', path, headers, data, cert)

    def delete(self, path, headers=None, data=None, cert=None):
        return self.call('DELETE', path, headers, data, cert)

#
# Usage Example:
#   import apsapi
#   aapi = apsapi.API(url = 'https://a.bvt.aps.sw.ru:6308')
#   resp = aapi.GET( '/aps/2/resources/' + safilter, self.getProviderToken() )
#
