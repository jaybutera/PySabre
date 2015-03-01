import HTTPCall

class TravelSeasonality(object):
    def __init__(self):
        self.HandleREST = HTTPCall.HTTPCall()
        self.HandleREST.request_authentication()
        self.tasks = {}

    def call(self):
        self.response = self.HandleREST.request_content( '/v1/historical/flights/JFK/seasonality ' + \
                '&'.join([task[0] for task in self.tasks.values() if task[1]]))

        # Return JSON content
        return self.response
