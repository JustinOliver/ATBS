# A dumb program to learn and mess around with command line

while True:
	try:
		x = int(input('give me an int: '))
	except ValueError:
		print ('Dont be an idiot')
		continue
	else:
		break
if x < 4:
	print ('less than 4')
elif x == 4:
	print ("egual 2 4")
else:
	print ('thats a big number')
print("your number is {}" .format(x))
print("Count to {} with me!" .format(x))
for num in range(x + 1):
	print(num)
print("Weee, that was fun!")
print("Now lets count backwards!")
for num1 in reversed(range(x + 1)):
	print(num1)
print("haha, I can't believe that worked")
