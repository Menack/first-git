
#Just getting the actual time.
import datetime
from turtle import title
e = datetime.datetime.now()
#Asking user's name, and printing name + date + time and remove WS and Capt.
name = input("Whats ur name pal? ").title().strip()
print ("Hi " + name + ", how was your day?" + ". ", end="")
print ("Today's date and time is: %s/%s/%s." % (e.day, e.month, e.year)," %s:%s:%s" % (e.hour, e.minute, e.second))




