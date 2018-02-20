#! python3
# stopwatch.py - A simple stopwatch program.

from time import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
starttime = time()
lasttime = starttime
lapnum = 1

try:
    while True:
        input()
        laptime = round(time() - lasttime, 2)
        totaltime = round(time() - starttime, 2)
        print('Lap #%s: Last Lap :%s Total Time: (%s)' % (lapnum, laptime, totaltime), end='')
        lapnum += 1
        lasttime = time()

except KeyboardInterrupt:
    print('\nDone.')

    
        
