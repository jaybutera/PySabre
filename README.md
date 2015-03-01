## PySabre
#### A comprehensive python library for Sabre's REST API

PySabre serves to provide Python users with an easy to use tool to access
Sabre's REST API through functions. No need to deal with URLs or Python's
Urllib(s).

Best of all, no dependencies!

An example call to the Leap Price Calendar API
'''
import PySabre.LeadPriceCalendar as LPC

cal = LPC.LeadPriceCalendar()

cal.origin('ATL')
cal.destination('LAS')
cal.lengthofstay([3,2])

# Return the JSON response, independent responses are also available from LPC's methods
print cal.call()
'''
