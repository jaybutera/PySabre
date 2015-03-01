import LeadPriceCalendar as LPC

cal = LPC.LeadPriceCalendar()

cal.getTasks()

cal.origin('DFW')
cal.destination('ATL')
cal.lengthofstay([3,4])

print(cal.call())

