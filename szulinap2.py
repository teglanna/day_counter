import datetime
import dateutil.parser

when = raw_input('When did you born?')
birthday = dateutil.parser.parse(when)
#birthday = datetime.date(2013,04,20)
print birthday
today = datetime.datetime.now()


print 'You have: ',today-birthday, 'days until your next birthday!'
