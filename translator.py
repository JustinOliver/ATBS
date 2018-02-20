#! python3
# translator.py - A program that takes text from a foriegn language webpage and translates page to english

import pyperclip, bs4, requests

# Ask user for webpage to use, or user can say to use text pasted on clipboard

address = input('What is the link to the webpage?\n If you have the address already on the clipboard, enter "clipboard".\n Otherwise, type address here:')

if address.lower() == "clipboard":
    address = pyperclip.paste()
    

# Give a print statement for the anxious

print('Getting information from: {}, \n please be patient' .format(address))
res=requests.get(address)

# Make sure it got the element okay, if something went wrong, throw exception and end program
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

text = soup.get_text()

print(text)












