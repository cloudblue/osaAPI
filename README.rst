paAPI
========

A python client for the Parallels Operations Automation (POA) and Parallels Business Automation Enterprise (PBA) APIs.

.. contents::
    :local:
    

============
Installation
============

Using pip::

    $ pip install paAPI
    

=============================
Connecting and Authenticating
=============================

.. code:: python

    POA(host,user=None,password=None,ssl=False,verbose=False,port=8440)
    
    PBA(host,user=None,password=None,ssl=False,verbose=False,port=5224)


Default Connection
------------------

.. code:: python

    from paAPI import POA, PBA

    # connect to POA
    pem = POA('mn.hostname.com')
    
    # connect to PBA
    api = PBA('pba.hostname.com')

Basic HTTP Authentication
-------------------------

.. code:: python

    from paAPI import POA, PBA
    
    # connect to POA 
    pem = POA('mn.hostname.com', user='admin', password='setup')
    

SSL
---

.. code:: python

    from paAPI import POA, PBA
    
    # connect to POA 
    pem = POA('mn.hostname.com', ssl=True)
    
Custom Port
-----------

.. code:: python

    from paAPI import POA, PBA
    
    # connect to POA 
    pem = POA('mn.hostname.com', port=8888)

=========================================
Parallels Operations Automation (POA) API
=========================================

All but three of the POA API calls start with 'pem', for this reason it is recommended you name your POA connection object 'pem' so you can call functions exactly how they are documented in the POA API as has been done in the examples in this Readme.

The full POA Public API Reference can be found here:

http://download.pa.parallels.com/poa/5.5/doc/index.htm?fileName=56781.htm

Basic API Call
--------------

This example will show the pem.getAccountInfo_ method being called.

.. _pem.getAccountInfo: http://download.pa.parallels.com/poa/5.5/doc/7915.htm

.. code:: python

    from paAPI import POA

    pem = POA('mn.hostname.com', port=8888)
    
    d = {
        'account_id' : 1002242
    }
    
    print pem.getAccountInfo(**d)
    
    # {'status': 0, 'result': {'fax': {'phone_num': '', 'ext_num': '', 'area_code': '', 'country_code': ''}, 'account_type': 'C', 'phone': {'phone_num': '00000000', 'ext_num': '', 'area_code': '04', 'country_code': '61'}, 'brand': {'brand_id': 191, 'domain_name': 'brandingdomain.com', 'name': 'brandname'}, 'email': 'noreply@example.com', 'person': {'first_name': 'John', 'last_name': 'Smith', 'middle_name': '', 'company_name': 'Test Account', 'title': ''}, 'address': {'city': 'Canberra', 'country': 'au', 'street_name': '1 Test Street', 'zipcode': '2621', 'state': 'ACT', 'house_num': '', 'address2': ''}, 'parent_account_id': 1002241}}

API Call with 'array of struct'
-------------------------------

The POA API often calls for values and settings to be sent as an 'array of struct'. This example shows how to send these values using the paAPI client.

This example is based on the pem.activateSubscription_ method with resources types called 'DiskSpace' and 'Bandwidth' and a domain name.

.. _pem.activateSubscription: http://download.pa.parallels.com/poa/5.5/doc/39160.htm

.. code:: python

    from paAPI import POA

    pem = POA('mn.hostname.com', port=8888)
    
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


Transactions
------------

There are three POA API calls that do not start with pem in the official documentation. When using paAPI you can use these API calls as documented but you will still need to preface them with your POA connection object (the examples on this page use 'pem' as the connection object name).
    
.. code:: python

    from paAPI import POA

    pem = POA('mn.hostname.com', port=8888)
    
    # being transaction
    pem.txn.Begin()
    
    # commit transaction
    pem.txn.Commit()
    
    # rollback transaction
    pem.txn.Rollback()
   
   
Error Handling
--------------

The POA API has quite good responces when an error occurs during an API call. The below example shows the responce format for POA API errors:


.. code:: python

    {
        'status'         : -1, 
        'extype_id'      : 21, 
        'module_id'      : 'OpenAPI', 
        'error_message'  : 'Invalid set of arguments. There should be specified EITHER external_info OR person, address, phone, [fax], [locale], email.', 
        'properties'     : { 
                               'reason': 'Invalid set of arguments. There should be specified EITHER external_info OR person, address, phone, [fax], [locale], email.'
                           }
    }

   
==================================================
Parallels Business Automation (PBA) API
==================================================

The PBA API is quite different from the POA API, and not quite as user friendly. The paAPI client makes using the PBA a little easier by standardizing the returned responces, providing status codes, and decoding any error messages.

The major difference between the POA and PBA api is how values are sent and received. In PBA params are sent and responces are received as a list in a specific order to know what each value represents.

The full PBA Public API Reference can be found here:

http://download.pa.parallels.com/pba/5.5/doc/pdf/SDK_API/pba_5.5_public_api_reference.pdf

Basic API Call
--------------

This example will show the **AccountDetailsGet_API** method being called.

.. code:: python

    from paAPI import PBA
    
    api = PBA('pba.hostname.com')
    
    print api.Execute('AccountDetailsGet_API', params=['1002242'])
    
    # {'status': 0, 'result': [1002242, 1002241, 'Test Account  5543', '1 Test Street', '', 'Canberra', '', '2621', 'au', '', 'John', 'D', 'Smith', 'noreply@example.com', '61', '04', '000000000', '', '', '', '', '', 1351787114, 2, 0]}
    
Alternate Server
----------------

Most PBA API method calls use the "BM" server. Some methods use alternate servers such as "PEMGATE" or "DOMAINGATE". This example shows how to specify an alternate server:

.. code:: python

    from paAPI import PBA
    
    api = PBA('pba.hostname.com')
    
    api.Execute('DomainExpirationDateGet_API', params=params, server='DOMAINGATE')
    
Error Handling
--------------

paAPI takes the way POA returns errors natively and applies it to the PBA API. The status on each responce will either be **0** for a succesfull call, or **-1** if PBA returned an error.

This is an example of what is returned in the case of an error:

.. code:: python

    {
        'status'        : -1, 
        'error_message' : 'Table Account does not contain row with ID 99999999.', 
        'server'        : 'BM', 
        'host'          : 'pba.hostname.com', 
        'params'        : ['99999999'], 
        'result'        : None, 
        'method'        : 'AccountDetailsGet_API'
    }

    

