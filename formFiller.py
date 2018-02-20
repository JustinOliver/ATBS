#! python3
# formFiller.py - Automatically fills in the form.

import pyautogui
from time import sleep

#Set these to the correct coordinates for your computer
nameField = (381,112)
submitButton = (374,604)
submitButtonColor = (74,140,247)
submitAnotherLink = (527,223)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
           ]
pyautogui.PAUSE = 0.5

for person in formData:
    # Give user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    sleep(5)

    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])

    #Fill out Name field.
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out great fear filed.
    pyautogui.typewrite(person['fear'] + '\t')

    # Fill out the source of wizard powers field
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

    # Fill out the Robocop field.
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # Fill out the additional comments field.
    pyautogui.typewrite(person['comments']+ '\t')

    # Cluck Submit
    pyautogui.press('enter')

    # Wait for for form page to load
    print('Clicked Submit.')
    sleep(5)

    # Click the submit another response link.
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])

