import json
import urllib, urllib2
import base64
import config

class HTTPCall(object):
    def __init__(self):
        # Determine user access token or assign standard test if not specified
        if not config.access_token:
            self.access_token = self.request_authentication()
        else:
            self.access_token = \
                    'Shared/IDL:IceSess\/SessMgr:1\.0.IDL/Common/!ICESMS\/ACPCRTD!ICESMSLB\/CRT.LB!-0123456789012345678!123456!0!ABCDEFGHIJKLM!E2E-1'

    def request_authentication(self):
        '''
        Performs HTTP authentication request.
        Returns user specific access token.
        '''
        # Initialization information
        encodedUserInfo = base64.b64encode(config.clientID)
        encodedPassword = base64.b64encode(config.password)

        encodedSecurityInfo = base64.b64encode( \
                encodedUserInfo + ':' + encodedPassword)

        # Authentication request setup
        data = {'grant_type': 'client_credentials'}
        headers = {                                                   \
                'content-type' : 'application/x-www-form-urlencoded', \
                'Authorization': 'Basic ' + encodedSecurityInfo       \
                }

        # Request authentication
        data = urllib.urlencode(data)
        request = urllib2.Request(config.auth_url, data, headers)
        response = json.loads(urllib2.urlopen(request).read())

        # Return access token
        return response['access_token']

    def request_content(self, call):
        # Authenticated content setup
        header = { \
                'Authorization': 'Bearer ' + str(self.access_token) \
                }
        request = urllib2.Request( \
                config.sabre_url + call, \
                None,                    \
                header                   \
                )

        # Request authenticated content
        result = urllib2.urlopen(request)

        return json.loads(result.read())
