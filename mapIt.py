#! python3
# mapIt.py - Launches a map in the browswer using an address 

import webbrowser, pyperclip, sys
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
