def time24hr(tstr):

	a = tstr.split(':')
	am = {'12':'00','1':'01','2':'02','3':'03','4':'04','5':'05','6':'06',
	      '7':'07','8':'08','9':'09','10':'10','11':'11'}
	pm = {'12':'12','1':'13','2':'14','3':'15','4':'16','5':'17','6':'18',
	      '7':'19','8':'20','9':'21','10':'22','11':'23'}

	# am or pm
	if len(tstr) == 7:
		periodOfTime = tstr[5:]
	elif len(tstr) == 6:
		periodOfTime = tstr[4:]

	periodOfTime = periodOfTime.lower()
	
	# remove the ':' character
	newTime = tstr.replace(":", "")
	
	# remove the 'am' or 'pm' chars in order to put 'hr' character instead.
	newTime = newTime.replace(periodOfTime, "") 
	
	# replace the string '12' with '00' if it's AM.
	if periodOfTime == 'am' or periodOfTime == 'AM':
		return am[a[0]] + a[1][:2] + 'hr'
	elif periodOfTime == 'pm' or periodOfTime == 'PM':
		return pm[a[0]] + a[1][:2] + 'hr'

print time24hr('12:34pm')
