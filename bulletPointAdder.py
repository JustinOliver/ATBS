#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()
print(text) # for testing
# Seperate lines and add stars
lines = text.split('\n')
print(lines) # for testing
for i in range(len(lines)):       # loop through all indexes in the "lines" list
	lines[i] = '* ' + lines[i]    # add star to each strin in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
print(text) # for testing