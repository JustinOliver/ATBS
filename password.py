#! python3

"""An attempt to make a password locker (note this is not secure, just an attempt to understand concepts)"""

PASSWORDS = {'email': 'whosajiggawhat',
			  'blog': 'password2',
			 'luggage': '21345'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)

