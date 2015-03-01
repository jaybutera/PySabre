# PySabre
#### A comprehensive python library for Sabre's REST API

PySabre serves to provide Python users with an easy to use tool to access
Sabre's REST API through functions. No need to deal with URLs or Python's
Urllib(s).

Best of all, no dependencies!

An example call to the Leap Price Calendar API
```python
import PySabre.LeadPriceCalendar as LPC

cal = LPC.LeadPriceCalendar()

cal.origin('ATL')
cal.destination('LAS')
cal.lengthofstay([3,2])

# Return the JSON response, independent responses are also available from LPC's methods
print cal.call()
```

Object operations emphasize the usefulness of handling REST data through a
Python library.
For example, given two LPC objects cal1 and cal2:
```python
>>> print cal1 > cal2
>>> True
```

This metric is a convenient way to compare the lowest fare cost of two separate
price calendars.
