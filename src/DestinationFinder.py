import HTTPCall

class DestinationFinder(object):
    def __init__(self):
        self.HandleREST = HTTPCall.HTTPCall()
        self.HandleREST.request_authentication()

        self.tasks = {  \
            'origin'                : ['origin=', False], \
            'location'              : ['location=', False],\
            'theme'                 : ['theme=', False],\
            'minfare'               : ['minfare=', False],\
            'maxfare'               : ['maxfare=', False],\
            'pointofsalecountry'    : ['pointofsalecountry=', False],\
            'departuredate'         : ['departuredate=', False],\
            'region'                : ['region=', False],\
            'returndate'            : ['returndate=', False],\
            'lengthofstay'          : ['lengthofstay=', False],\
            'earliestdeparturedate' : ['earliestdeparturedate=', False],\
            'latestdeparturedate'   : ['latestdeparturedate=', False]}

        self.response = {}

    #############################
    #                           #
    #          REQUEST          #
    #                           #
    #############################


    def origin(self, org):
        '''
        Adding the user input to origin string 
        '''
        self.tasks['origin'][1] = True
        self.tasks['origin'][0] += org

    def location(self, loc):
        '''
        Adding the user input to destination string 
        '''
        self.tasks['location'][1] = True
        self.tasks['location'][0] += loc

    def theme(self, thme):
        '''
        Adding the user input to lengthofstay string 
        '''
        self.tasks['theme'][1] = True
        self.tasks['theme'][0] += ','.join(thme)

    def minfare(self, mnfare):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['lengthofstay'][1] = True
        self.tasks['lengthofstay'][0] += ','.join(mnfare)

    def maxfare(self, mxfare):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['maxfare'][1] = True
        self.tasks['maxfare'][0] += ','.join(mxfare)

    def pointofsalecountry(self, pcountry):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['pointofsalecountry'][1] = True
        self.tasks['pointofsalecountry'][0] += ','.join(pcountry)

    def region(self, regon):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['region'][1] = True
        self.tasks['region'][0] += ','.join(regon)

    def topdestinations(self, topdest):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['topdestinations'][1] = True
        self.tasks['topdestinations'][0] += ','.join(topdest)

    def departuredate(self, depart):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['departuredate'][1] = True
        self.tasks['departuredate'][0] += depart

    def returndate(self, returnd):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['returndate'][1] = True
        self.tasks['returndate'][0] += returnd

    def lengthofstay(self, lstay):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['lengthofstay'][1] = True
        self.tasks['lengthofstay'][0] += ','.join(lstay)

    def earliestdeparturedate(self, edepart):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['earliestdeparturedate'][1] = True
        self.tasks['earliestdeparturedate'][0] += ','.join(edepart)

    def latestdeparturedate(self, ldepart):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['latestdeparturedate'][1] = True
        self.tasks['latestdeparturedate'][0] += ','.join(ldepart)     

    ### Query ###
    def call(self):
                self.response = self.HandleREST.request_content( '/v1/shop/flights/fares?' + \
                '&'.join([task[0] for task in self.tasks.values() if task[1]]))
        # Return JSON content
        return self.response
