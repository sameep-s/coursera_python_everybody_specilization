#this is the assignment
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
print('---------------------------------------------------------------------------------')
for line in handle:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    words = line.split()
    words = words[1]
    print(words)
    counts[words] = counts.get(words, 0) + 1
print('---------------------------------------------------------------------------------')

          
bigcount = None
bigword = None
           
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigcount = count
		bigword = word

print(bigword, bigcount)
