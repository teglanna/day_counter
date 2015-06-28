from datetime import date

yearnow = date.today().year
monthnow = date.today().month
daynow = date.today().day
lst = [yearnow, monthnow, daynow]

when = (input('When did you born? (year,month,day)'))
#print (when)
yearthen = int(when[0])
monththen = int(when[1])
daythen = int(when[2])
#print (monththen)

def is_leap_year(yearnext):
	if yearnext % 4 == 0 or yearnext % 400 == 0 and yearnext % 100 != 0:
		return True
	return False	

monthdays = [0,31,28,31,30,31,30,31,31,30,31,30,31]

if monththen < monthnow:
	monthdays_this_year = monthdays[monthnow:]
	#print (monthdays_this_year)
	monthdays_next_year = monthdays[0:monththen]
	#print (monthdays_next_year)
	in_this_year = sum(monthdays_this_year)-daynow
	in_next_year = sum(monthdays_next_year)+daythen
	result = (in_this_year + in_next_year)

	if is_leap_year(yearnow+1) == True:
		result += 1
	print ('You have: ',result, 'days until your next birthday!')
	#res = 'You have: ',result, 'days until your next birthday!'
#print (sum(monthdays_this_year)-daynow)
#print (sum(monthdays_next_year)+daythen)

if monththen >= monthnow:
	result = sum(monthdays[monthnow:monththen])-daynow+daythen
	print ('You have: ',result, 'days until your next birthday!')


remainder = result % 7	
weeks = int((result - remainder) / 7)
print (weeks, 'weeks and ', remainder, 'days')


