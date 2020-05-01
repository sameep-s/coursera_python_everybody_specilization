'''
numList = []

while True:
	value = input('Please enter a number:')
	if value == 'done': break
	nValue = float(value)
	numList.append(nValue)

average = sum(numList) / len(numList)
print('The average of these numbers is:', average)
'''
h = 'List after remove() method'
stuff = h.split()
for w in stuff:
	print(w)

fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	if not line.startswith('From'): continue
	words = line.split()
	print(words[2])