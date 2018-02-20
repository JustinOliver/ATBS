#!python3

# -Mario.py recreating something I learned in CS50 trying to refresh some basic concepts

# Ask for height, which can be between 1 and 23

while True:
    x = int(input("How tall do you want it to be?:"))
    if x < 1 or x > 50000000:
        print("Your height must be between 1 and 23")
    else:
        break
    
row ='#'
space = ' '
top = 'A'
print(space * (x), end ='')
print(top)
for i in range(1, x+ 1):
    print(space * (x - i), end='')
    print(row * (i), end ='')
    print(row * (i))
