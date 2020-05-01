##using while loop
fruit = 'bananna'
index = 0
while index < len(fruit):
	letter = fruit[index]
	print(index, letter)
	index = index + 1
'''
#using for loop
fruit = 'bananna'
for letter in fruit:
	print(letter)
'''

print(fruit[4:6])

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])