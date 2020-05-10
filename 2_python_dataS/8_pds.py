name = input('Enter a file name:')
handle = open(name)

counts = dict()
for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1

bigCount = None
bigWord = None
#print(counts.items())

for word,count in counts.items():
	if bigCount is None or count > bigCount:
		bigCount = count
		bigWord = word

print(bigWord)
print(bigCount)