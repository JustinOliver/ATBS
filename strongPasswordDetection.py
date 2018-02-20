#! python3
# strongPasswordDetection.py - determines if password is strong (8 chars, both upper and lower, and at least one int)

import re

def strongPW(text):
	Len = re.compile(r'\w{8,}')		# Make sure length is 8 or more
	low = re.compile(r'[a-z]')		# Make sure there is at least 1 lowercase
	CAP = re.compile(r'[A-Z]')		# Make sure there is at least 1 uppercase
	digit = re.compile(r'\d')		# Make sure there is at least one digit			
	
	mo1 = Len.search(text)
	mo2 = CAP.search(text)
	mo3 = low.search(text)
	mo4 = digit.search(text)
	
	if mo1 == None or mo2 == None or mo3 == None or mo4 == None:
		print('Oops, your password is not strong enough!')
	else:
		print('Nice password homie! Your password is ' + text)


test = input('What do you want your password to be?: ')
strongPW(test)