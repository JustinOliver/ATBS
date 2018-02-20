#! python3
# 2048.py - A program to automate the game 2048 from the webpage remotely

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')  
time.sleep(10)                                                                          # Give page time to load
body = browser.find_element_by_tag_name('body')                                         # Select area for arrow keys to function
turns = 0
times = input('How many times do you want the game to run?:')
for i in range (int(times)):
    print('Game is running....')
    while True:
        body.send_keys(Keys.UP)
        #time.sleep(4)                                                                  # Give time to view moves, if desired remove comment hash
        body.send_keys(Keys.RIGHT)
        #time.sleep(4)
        body.send_keys(Keys.DOWN)
        #time.sleep(2)
        body.send_keys(Keys.LEFT)
        #time.sleep(2)
        turns += 4
        try:
            status = browser.find_element_by_class_name('game-message.game-over')
            time.sleep(1)                                                              # give it time to compute final score, otherwise you end up with goofy text       
            score = browser.find_element_by_class_name('score-container')
            score_t = score.text
            print('Game over! That went {} turns for a score of {}'.format(turns, score_t))
            break
        except:
            continue
    turns = 0
    retry = browser.find_element_by_class_name('retry-button')
    retry.click()


