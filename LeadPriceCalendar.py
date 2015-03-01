class LeadPriceCalendar(object):
    def __int__(self):
        self.tasks = {  \
            'origin'        : ('origin=', False), \
            'destination'   : ('destination=', False)\
            'lengthofstay'  : ('lengthofstay=', False)\
            'departuredate' : ('departuredate=', False)\
            'minfare'       : ('minfare=', False)\
            'maxfare'       : ('maxfare=', False)}

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

    
