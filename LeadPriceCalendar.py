class LeadPriceCalendar(object):
    def __int__(self):
        self.tasks = {  \
            'origin'        : ('origin=', False), \
            'destination'   : ('destination=', False)\
            'lengthofstay'  : ('lengthofstay=', False)\
            'departuredate' : ('departuredate=', False)\
            'minfare'       : ('minfare=', False)\
            'maxfare'       : ('maxfare=', False)}
        self.response = {}

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
    '''
    def shop_link(self):
        return self.response['ShopLink']
    def self(self):
        return self.response['']
    def link_template(self):
        return self.response[]
    '''
    
    '''
    '''
    def origin(self, org):
        '''
        Adding the user input to origin string 
        '''
        self.tasks['origin'][1] = True
        return 'origin=' += org

    def destination(self, dest):
        '''
        Adding the user input to destination string 
        '''
        self.tasks['destination'][1] = True
        return 'destination=' += dest

    def lengthofstay(self, length):
        '''
        Adding the user input to lengthofstay string 
        '''
        self.tasks['lengthofstay'][1] = True
        return 'lengthofstay=' += ','.join(length)

    def departuredate(self, depart):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['departuredate'][1] = True
        return 'departuredate=' += ','.join(depart)

    def minfare(self, minf):
        self.tasks['minfare'][1] = True
        return minf

    def maxfare(self, maxf):
        self.tasks['maxfare'][1] = True
        return maxf

    def pointofsalecountry(self, countryCode):
        self.tasks[6] = True
        return countryCode

    def leadCall(self):            
        if tasks['departuredate'][1]:
            assert tasks['lengthofstay'][1].count(',') < 5
        else:
            assert tasks['lengthofstay'][1].count(',') < 10
