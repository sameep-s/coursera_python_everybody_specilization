jist = [1,1,3,4,[2,6,7,],6]
print('This is the fuckin list:' ,jist[1:5])
x = input('Give an input to push into the list:')
#try and except block to make program more versatile
try:
	if type(x) == str:
		y = float(x)
except:
	y = x

jist.append(y)
print('List after append() method' ,jist)
jist.remove(y)
print('List after remove() method' ,jist)


friends = ['Joseph', 'Glenn', 'Sally']
'''
for friend in friends:
	print('Happy New Year:', friend)
'''
for i in range(len(friends)):
	friend = friends[i]
	print('Happy New Year:', friend)