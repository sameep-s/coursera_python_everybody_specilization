'''
#The use of while loop
while True:
	line = input('> ')
	if line[0] == '#' :
		continue
	if line == 'done' :
		break
	print(line)
print('Done!')
'''
'''
for i in {1,3,3,4,5,6,7,8}:
	print(i+1)
print('Blastoff!!')
'''
'''
print('Before')
for thing in [9,41,12,3,74,15]:
	print(thing)
print('After')
'''


'''
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15] :
	if the_num > largest_so_far :
		largest_so_far = the_num
	print(largest_so_far, the_num)

print('After', largest_so_far)
'''
'''
found = False
print('Before', found)
for values in [9,41,12,3,74,15]:
	if values == 3:
		found == True
	print(found, values)
print('After', found)

smallest_so_far = None
print('Before', smallest_so_far)
for the_num in [9,41,12,3,74,15] :
	if smallest_so_far is None :
		smallest_so_far = the_num
	elif the_num < smallest_so_far:
		smallest_so_far = the_num
	print(smallest_so_far, the_num)

print('After', smallest_so_far)
tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)
'''

largest = None
smallest = None
while True:
	num = input('Enter a number:')
	n = 0


	if num =='done':
		break
	try:
		rnum = float(num)
	except:
		print('Please a valid input:')

	if largest is None:
		largest = rnum
	elif largest < rnum:
		largest = rnum

	if smallest is None:
		smallest = rnum
	elif smallest > rnum:
		smallest = rnum

print("Maximum", largest)
print("Minimum", smallest)
print('No. of times wrong input entered:', n)

