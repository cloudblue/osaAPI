import httplib
import json
import ssl
import urllib2
from urlparse import urljoin


class HTTPSClientAuthHandler(urllib2.HTTPSHandler, object):
    def __init__(self, key, cert, context=None):
        super(HTTPSClientAuthHandler, self).__init__(context=context)
        self.key = key
        self.cert = cert

    def https_open(self, req):
        # Rather than pass in a reference to a connection class, we pass in
        # a reference to a function which, for all intents and purposes,
        # will behave as a constructor
        return self.do_open(self.get_connection, req)

    def get_connection(self, host, timeout=300):
        return httplib.HTTPSConnection(host, key_file=self.key, cert_file=self.cert, context=self._context)


class API(object):
    def __init__(self, url, use_unverified_context):
        """
        Takes something like the following argument as input:
        url = 'https://a.bvt.aps.sw.ru:6308'
        """
        self.url = url
        self.use_unverified_context = use_unverified_context

    def call(self, verb, path, headers=None, data=None, cert=None):
        data = json.dumps(data)

        url = urljoin(self.url, path)
        if not headers:
            headers = dict()

        req = urllib2.Request(url, headers=headers, data=data)
        req.get_method = lambda: verb

        context = None
        if self.use_unverified_context:
            context = ssl._create_unverified_context()

        try:
            if cert:
                opener = urllib2.build_opener(HTTPSClientAuthHandler(cert, cert, context=context))
                resp = opener.open(req)
            else:
                resp = urllib2.urlopen(req, context=context)
        except urllib2.HTTPError as error:
            content = error.read()

            # APS Exceptions have the following structure (example):
            # {
            #    "code": 500,
            #    "type": "APS::Hosting::Exception",
            #    "message": "Limit for resource ..."
            # }
            # In order to allow simple processing of this exception like
            # ('something' in error.aps.message) we convert this exception
            # to JSON directly here.
            if content:
                error.aps = json.loads(content)
            else:
                error.aps = {'code': 0, 'type': '', 'message': ''}
            raise error

        content = resp.read()

        # Converting JSON immediately if presented
        if content:
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
