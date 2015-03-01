class LeadPriceCalendar(object):
    def __int__(self):
        self.tasks = {  \
            'origin'                 : ('origin=', False), \
            'destination'            : ('destination=', False),\
            'earliestdeparturedate'  : ('earliestdeparturedate=', False),\
            'latestdeparturedate'    : ('latestdeparturedate=', False),\
            'lengthofstay'           : ('lengthofstay=', False),\
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
    '''
    def origin(self, org):
        '''
        Adding the user input to origin string 
        '''
        self.tasks['origin'][1] = True
        return 'origin=' + org

    def earliestdeparturedate(self, dest):
        '''
        Adding the user input to destination string 
        '''
        self.tasks['earliestdeparturedate'][1] = True
        return 'earliestdeparturedate=' + dest

    def latestdeparturedate(self, length):
        '''
        Adding the user input to lengthofstay string 
        '''
        self.tasks['latestdeparturedate'][1] = True
        return 'latestdeparturedate=' + ','.join(length)

    def lengthofstay(self, depart):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['lengthofstay'][1] = True
        return 'lengthofstay=' + ','.join(depart)


    #def leadCall(self):            

