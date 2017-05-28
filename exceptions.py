try:
	count = int(input("Give me a number: "))
except ValueError:
	print("That's not a number idiot!!")
else:
	print("Hi " * count)

