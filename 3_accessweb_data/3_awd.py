#Assignment1, week2

import re
fh = open('act_data.txt')
x = list()
i = 0
for line in fh:
	y = re.findall('([0-9]+)', line)
	if len(y) == 0: continue
	n = 0
	while n < len(y):
		z = int(y[n])
		n = n + 1
		x.append(z)
		i = i + 1

print('The sum is:', sum(x))
print('Number of Items are: ', i)










'''
import re

sum = 0
n = 0

file = open('act_data.txt', 'r')
for line in file:
    numbers = re.findall('[0-9]+', line)
    if not numbers:
        continue
    else:
        for number in numbers:
        	print(number)
        	sum += int(number)
        	n = n+1
print('---------------------------------')
print('n is:',n)
print(sum)
'''