import HTTPCall

class LeadPriceCalendar(object):
    def __init__(self):
        self.HandleREST = HTTPCall.HTTPCall()
        self.HandleREST.request_authentication()

        self.tasks = {  \
            'origin'                   : ['origin=', False], \
            'destination'              : ['destination=', False],\
            'lengthofstay'             : ['lengthofstay=', False],\
            'departuredate'            : ['departuredate=', False],\
            'minfare'                  : ['minfare=', False],\
            'maxfare'                  : ['maxfare=', False],\
            'pointofsalecountry'       : ['maxfare=', False]}

        self.response = {}

    def getTasks(self):
        print [task for task in self.tasks.values()]

    #############################
    #                           #
    #         RESPONSE          #
    #                           #
    #############################

    def origin_location(self):
        '''
        Returns a string
        '''
        return self.response['OriginLocation']
    def destination_location(self):
        '''
        Returns a string
        '''
        return self.response['DestinationLocation']
    def fare_info(self):
        '''
        Returns an array
        '''
        return self.response['FareInfo']
    def lowest_fare(self):
        '''
        Returns a string
        '''
        return self.response['LowersFare']
    def currency_code(self):
        '''
        Returns a string
        '''
        return self.response['CurrencyCode']
    def lowerst_nonstop_fare(self):
        '''
        Returns a string
        '''
        return self.response['LowestNonStopFare']
    def departure_date_time(self):
        '''
        Returns a string
        '''
        return self.response['DepartureDateTime']
    def return_date_time(self):
        '''
        Returns a string
        '''
        return self.response['ReturnDateTime']
    def links(self):
        '''
        Returns an array
        '''
        return self.response['Links']

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

    def destination(self, dest):
        '''
        Adding the user input to destination string 
        '''
        self.tasks['destination'][1] = True
        self.tasks['destination'][0] += dest

    def lengthofstay(self, length):
        '''
        Adding the user input to lengthofstay string 
        '''
        self.tasks['lengthofstay'][1] = True
        self.tasks['lengthofstay'][0] += ','.join(length)

    def departuredate(self, depart):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['departuredate'][1] = True
        self.tasks['departuredate'][0] += ','.join(depart)

    def minfare(self, minf):
        self.tasks['minfare'][1] = True
        self.tasks['minfare'][0] += minf

    def maxfare(self, maxf):
        self.tasks['maxfare'][1] = True
        self.tasks['maxfare'][0] += maxf

    def pointofsalecountry(self, countryCode):
        self.tasks['pointofsalecountry'][1] = True
        self.tasks['pointofsalecountry'][0] += countryCode

    ### Call Function ###

    def call(self):
        if self.tasks['departuredate'][1]:
            assert self.tasks['lengthofstay'][0].count(',') < 5
        else:
            assert self.tasks['lengthofstay'][0].count(',') < 10

        self.response = self.HandleREST.request_content( '/v1/shop/flights/fares?' + \
                '&'.join([task[0] for task in self.tasks.values() if task[1]]))

        # Return JSON content
        return self.response
