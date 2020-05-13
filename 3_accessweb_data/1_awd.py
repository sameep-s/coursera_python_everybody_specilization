import re
x = 'My favourite 2 numbers are 19 and 42.'
han = open('mbox-short.txt')
print(x)
y = re.findall('[0-9]+' ,x)
print(y)
y = re.findall('[aeiou]+' ,x)
print(y)

#1055 84%
#Example of greedy matching,It matches the longest possible string.
x2 = 'From: Using the : character'
y = re.findall('^F.+:', x2)
print(y)
y = re.findall('^F.+?:', x2)
print(y)


print('----------------------------------------------')
for line in han:
	if not line.startswith('From '): continue
	y = re.findall('\S+@\S+' ,line)
	print(y)
	y = re.findall('@[^ ]*' ,line)
	print(y)
	print('------------------------------------------')

