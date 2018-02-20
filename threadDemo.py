import threading, time
print('Start of program! How exciting!')

def takeANap():
    time.sleep(5)
    print('Wake up yo!')

threadObj = threading.Thread(target=takeANap)
print('has anything started yet?')
threadObj.start()


print('End of program')
