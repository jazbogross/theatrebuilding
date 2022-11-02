import datetime

now = datetime.datetime.now()

print
print "Current date and time using str method of datetime object:"
print str(now)

print
print "Current date and time using instance attributes:"
print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond

print
print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")
The result:

Current date and time using str method of datetime object:
2013-02-17 16:02:49.338517

Current date and time using instance attributes:
Current year: 2013
Current month: 2
Current day: 17
Current hour: 16
Current minute: 2
Current second: 49
Current microsecond: 338517

Current date and time using strftime:
2013-02-17 16:02
