import HTTPCall

class LowFareForecast(object):
    def __init__(self):
        self.HandleREST = HTTPCall.HTTPCall()
        self.HandleREST.request_authentication()

        self.tasks = {  \
            'origin'        : ['origin=', False], \
            'destination'   : ['destination=', False],\
            'departuredate' : ['departuredate=', False],\
            'returndate'    : ['returndate=', False]}

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

    def highest_predicted_fare(self):
        '''
        Returns an int
        '''
        return self.response['highestPredictedFare']

    def lowest_predicted_fare(self):
        '''
        Returns an int
        '''
        return self.response['lowestPredictedFare']
    def lowest_fare(self):
        '''
        Returns a string/int 
        '''
        return self.response['lowestFare']
    def CurrecnyCode(self):
        '''
        Returns a string 
        '''
        return self.response['ReturnDateTime']
    def links_node_array(self):
        '''
        Returns an array
        '''
        return self.response['Links']

    ###########################
    #                         #
    #    Request Functions    #
    #                         #
    ###########################

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

    def departuredate(self, depart):
        '''
        Adding the user input to departuredate string 
        '''
        self.tasks['departuredate'][1] = True
        self.tasks['departuredate'][0] += depart
        #self.tasks['departuredate'][0] += '{0}-{1}-{2}'.format( \
        #        depart[:3], depart[4:5], depart[5:6])

    def returndate(self, rdate):
        '''
        Adding the user input to returndate string 
        '''
        self.tasks['returndate'][1] = True
        self.tasks['returndate'][0] += rdate
        #self.tasks['returndate'][0] += '{0}-{1}-{2}'.format( \
        #        rdate[:3], rdate[4:5], rdate[5:6])

    ### Call Function ###

    def call(self):
        # All tasks are required
        assert (False not in self.tasks.values()[1])

        print ('/v1/forecast/flights/fares?' + \
                    '&'.join([task[0] for task in self.tasks.values() if task[1]]))
        self.response = self.HandleREST.request_content('/v1/forecast/flights/fares?' + \
                    '&'.join([task[0] for task in self.tasks.values() if task[1]]))

        # Return JSON content
        return self.response
