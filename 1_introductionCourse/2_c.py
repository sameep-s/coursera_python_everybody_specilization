#convert elevator floor
try:
	inp = input('Europe Floor?')
	usf = int(inp) + 1
	print('US floor', usf)
	print('123' + 'abc')
except:
	print('Please enter a valid output:')

#this is just compairing of two numbers.
try:
	a = int(input('input a Number:'))

	if a > 10:
		print(a,'is greater than 10.')
	elif a < 10:
		print(a,'is less than 10.')
	elif a == 10:
		print(a,'is equal to 10.')
except:
	print('Enter a number between 1 and 10:')
