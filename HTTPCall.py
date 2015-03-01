import json
import urllib, urllib2
import base64
import config

class HTTPCall(object):
    def __init__(self):
        if config.access_token.isEmpty()
        self.access_token = request_authentication()

    def request_authentication(self):
        '''
        Performs HTTP authentication request.
        Returns user specific access token.
        '''
        # Initialization information
        encodedUserInfo = base64.b64encode(config.clientID)
        encodedPassword = base64.b64encode(config.password)

        encodedSecurityInfo = base64.b64encode( \
                encodeUserInfo + ':' + encodedPassword)

        # Authentication request setup
        data = {'grant-type': 'client_credentials'}
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

    def request_content(self, uri):
        # Authenticated content setup
        header = { \
                'Authorization': 'Bearer ' + str(self.access_token) \
                }
        request = urllib2.Request( \
                config.sabre_url + uri, \
                None,                   \
                header                  \
                )

        # Request authenticated content
        result = urllib2.urlopen(request)

        return json.loads(result.read())
