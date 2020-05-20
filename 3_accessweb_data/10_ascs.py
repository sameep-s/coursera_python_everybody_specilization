i = input('give value:')
i = int(i)
if i%5==0 and i%3==0:
	print('3')
elif i%3==0:
	print('1')
elif i%5==0:
	print('2')
else:
	print('0')