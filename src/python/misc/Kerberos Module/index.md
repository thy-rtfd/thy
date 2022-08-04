# Kerberos Module

hihi hahaha

## test123

The basic flow of a typical Kerberos authentication is as follows:

- Client sends an unauthenticated request to the server
- Server sends back a 401 response with a `WWW-Authenticate: Negotiate` header with no authentication details
- Client sends a new request with an `Authorization: Negotiate` header
- Server checks the `Authorization` header against the Kerberos infrastructure and either allows or denies access accordingly. If access is allowed, it should include a `WWW-Authenticate: Negotiate` header with authentication details in the reply.
- Client checks the authentication details in the reply to ensure that the request came from the server

My Sample Python code using kerberos module (You can use [requests-kerberos](https://github.com/requests/requests-kerberos) too):
```python
import requests
import kerberos
import dns.resolver

from requests.compat import urlparse

def myrequests_request(method, url, client_principal=None, **kwargs):
    req = requests.request(method, url, **kwargs)
    if "Negotiate" in req.headers.get("www-authenticate", ""):
        hostname = urlparse(req.url).hostname
        canonical_name = dns.resolver.Resolver().query(hostname).canonical_name
        ret_code, context = kerberos.authGSSClientInit(f"HTTP@{canonical_name}", principal=client_principal)
        kerberos.authGSSClientStep(context, "")
        kwargs["headers"] = {**kwargs.get("headers", {}), 
                             **{"Authorization": f"Negotiate {kerberos.authGSSClientResponse(context)}"}}
        req = requests.request(method, req.url, **kwargs)
    return req

myrequests_get = lambda url, **kwargs: myrequests_request('GET', url, **kwargs)
myrequests_post = lambda url, **kwargs: myrequests_request('POST', url, **kwargs)

req = myrequests_get("http://your.server.com/")
```
Before running above script, you need to obtain and cache Kerberos ticket-granting tickets (using kinit)

How to create keytab file and run kinit with it
```shell
kutil -v -k your.keytab.kt add -p User@your.domain -V 0 -e arcfour-hmac-md5
kinit -kt your.keytab.kt User@your.domain
```

References:
- [Using the Python Kerberos Module](http://python-notes.curiousefficiency.org/en/latest/python_kerberos.html)
- [requests-kerberos](https://github.com/requests/requests-kerberos)  
- [rfc4559: SPNEGO-based Kerberos and NTLM HTTP Authentication in Microsoft Windows](https://tools.ietf.org/html/rfc4559)
- [apple/ccs-pykerberos/pysrc/kerberos.py](https://raw.githubusercontent.com/apple/ccs-pykerberos/master/pysrc/kerberos.py)
- <https://web.mit.edu/kerberos/>
- <https://kb.iu.edu/d/aumh>

