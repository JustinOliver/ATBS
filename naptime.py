x = float(input("What time is it (in 24 hour decimal format)?: "))
if x > 21.00 and x < 22.00:
	print("Go to bed, its {:.2f} minutes past your bedtime" .format((x - 21.00) * 100))
elif x >= 22.00:
	print("It's over an hour past your bedtime, go to bed NOW!")
else:
	print("Keep on learning homie!")