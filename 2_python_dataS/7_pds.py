'''
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()
print('Words:', words)

print('Counting...')
for word in words:
	counts[word] = counts.get(word,0) + 1
print('Counts', counts)
'''

names = {'Sameep' : 22, 'Jerusalem' :3022, 'Saleem' : 55}
print('Using single variable in for loop:')
for key in names:
	print(key, names[key])
print(names.keys())
print(names.items())

print('Using two variables in for loop:')
for aaa,bbb in names.items():
	print(aaa, bbb)
	print('Lets see')