#this is the assignment
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
          
bigcount = None
bigword = None
print(counts.items())
           
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigcount = count
		bigword = word

print(bigword, bigcount)
