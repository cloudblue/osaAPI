osaAPI
=====
[![Build Status](https://travis-ci.org/odin-public/osaAPI.png?branch=master)](https://travis-ci.org/odin-public/osaAPI)

A python client for the Odin Service Automation (OSA) and billing APIs.

Installation
------------

Using pip:

    $ pip install osaAPI

Connecting and Authenticating
-----------------------------

``` {.sourceCode .python}
OSA(host,user=None,password=None,ssl=False,verbose=False,port=8440)

PBA(host,user=None,password=None,ssl=False,verbose=False,port=5224)
```

### Default Connection

``` {.sourceCode .python}
from osaapi import OSA, PBA

# connect to OSA
pem = OSA('mn.hostname.com')

# connect to PBA
api = PBA('pba.hostname.com')
```

### Basic HTTP Authentication

``` {.sourceCode .python}
from osaapi import OSA, PBA

# connect to OSA 
pem = OSA('mn.hostname.com', user='admin', password='setup')
```

### SSL

``` {.sourceCode .python}
from osaapi import OSA, PBA

# connect to OSA 
pem = OSA('mn.hostname.com', ssl=True)
```

### Custom Port

``` {.sourceCode .python}
from osaapi import OSA, PBA

# connect to OSA 
pem = OSA('mn.hostname.com', port=8888)
```

Odin Service Automation (OSA) API
-----------------------------------------

All but three of the OSA API calls start with 'pem', for this reason it
is recommended you name your OSA connection object 'pem' so you can call
functions exactly how they are documented in the OSA API as has been
done in the examples in this Readme.

The full OSA Public API Reference can be found here:

<http://download.pa.parallels.com/poa/5.5/doc/index.htm?fileName=56781.htm>

### Basic API Call

This example will show the
[pem.getAccountInfo](http://download.pa.parallels.com/poa/5.5/doc/7915.htm)
method being called.

``` {.sourceCode .python}
from osaapi import OSA

pem = OSA('mn.hostname.com')

d = {
    'account_id' : 1002242
}

print pem.getAccountInfo(**d)

# {'status': 0, 'result': {'fax': {'phone_num': '', 'ext_num': '', 'area_code': '', 'country_code': ''}, 'account_type': 'C', 'phone': {'phone_num': '00000000', 'ext_num': '', 'area_code': '04', 'country_code': '61'}, 'brand': {'brand_id': 191, 'domain_name': 'brandingdomain.com', 'name': 'brandname'}, 'email': 'noreply@example.com', 'person': {'first_name': 'John', 'last_name': 'Smith', 'middle_name': '', 'company_name': 'Test Account', 'title': ''}, 'address': {'city': 'Canberra', 'country': 'au', 'street_name': '1 Test Street', 'zipcode': '2621', 'state': 'ACT', 'house_num': '', 'address2': ''}, 'parent_account_id': 1002241}}
```

### API Call with 'array of struct'

The OSA API often calls for values and settings to be sent as an 'array
of struct'. This example shows how to send these values using the osaapi
client.

This example is based on the
[pem.activateSubscription](http://download.pa.parallels.com/poa/5.5/doc/39160.htm)
method with resources types called 'DiskSpace' and 'Bandwidth' and a
domain name.

``` {.sourceCode .python}
from osaapi import OSA

pem = OSA('mn.hostname.com')

# define the resource limits:
DiskSpace = {
    "resource_id" : 1002486,
    "resource_limit" : 1024
}
Bandwidth = {
    "resource_id" : 1002487,
    "resource_limit" : -1
}

# define the paramaters:
DomainName = {
    "var_name"  : "DomainID",
    "var_value" : "example.com.au"
}

# setup the call:
d = {
    "account_id"           : 1002242,
    "subscription_name"    : "Hosting (example.com.au)",
    "subscription_id"      : 1006754,
    "service_template_id"  : 204,
    "resource_limits"      : [DiskSpace, Bandwidth],
    "paramaters"           : [DomainName],
}

# execute the call:
result = pem.activateSubscription(**d)
```

### Transactions

There are three OSA API calls that do not start with pem in the official
documentation. When using osaapi you can use these API calls as
documented but you will still need to prefix them with your OSA
connection object (the examples on this page use 'pem' as the connection
object name).

``` {.sourceCode .python}
from osaapi import OSA

pem = OSA('mn.hostname.com')

# being transaction
pem.txn.Begin()

# commit transaction
pem.txn.Commit()

# rollback transaction
pem.txn.Rollback()
```

### Error Handling

The OSA API has quite good responces when an error occurs during an API
call. The below example shows the responce format for OSA API errors:

``` {.sourceCode .python}
{
    'status'         : -1, 
    'extype_id'      : 21, 
    'module_id'      : 'OpenAPI', 
    'error_message'  : 'Invalid set of arguments. There should be specified EITHER external_info OR person, address, phone, [fax], [locale], email.', 
    'properties'     : { 
                           'reason': 'Invalid set of arguments. There should be specified EITHER external_info OR person, address, phone, [fax], [locale], email.'
                       }
}
```

Billing module API
---------------------------------------

The billing API is quite different from the OSA API, and not quite as user
friendly. The osaapi client makes using the billing a little easier by
standardizing the returned responses, providing status codes, and
decoding any error messages.

The major difference between the OSA and billing api is how values are sent
and received. In billing params are sent and responses are received as a
list in a specific order to know what each value represents.

The full billing Public API Reference can be found here:

<http://download.pa.parallels.com/pba/5.5/doc/pdf/SDK_API/pba_5.5_public_api_reference.pdf>

### Basic API Call

This example will show the **AccountDetailsGet\_API** method being
called.

``` {.sourceCode .python}
from osaapi import PBA

api = PBA('pba.hostname.com')

print api.Execute('AccountDetailsGet_API', params=['1002242'])

# {'status': 0, 'result': [1002242, 1002241, 'Test Account  5543', '1 Test Street', '', 'Canberra', '', '2621', 'au', '', 'John', 'D', 'Smith', 'noreply@example.com', '61', '04', '000000000', '', '', '', '', '', 1351787114, 2, 0]}
```

### Alternate Server

Most billing API method calls use the "BM" server. Some methods use
alternate servers such as "PEMGATE" or "DOMAINGATE". This example shows
how to specify an alternate server:

``` {.sourceCode .python}
from osaapi import PBA

api = PBA('pba.hostname.com')

api.Execute('DomainExpirationDateGet_API', params=params, server='DOMAINGATE')
```

### Error Handling

osaapi takes the way OSA returns errors natively and applies it to the
billing API. The status on each responce will either be **0** for a
succesfull call, or **-1** if billing returned an error.

This is an example of what is returned in the case of an error:

``` {.sourceCode .python}
{
    'status'        : -1, 
    'error_message' : 'Table Account does not contain row with ID 99999999.', 
    'server'        : 'BM', 
    'host'          : 'pba.hostname.com', 
    'params'        : ['99999999'], 
    'result'        : None, 
    'method'        : 'AccountDetailsGet_API'
}
```
