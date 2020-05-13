import re
hand = open('mbox-short.txt')
numlist = list()
i = 0
j = 0
for line in hand:
	i = i+1
	line = line.rstrip()
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	if len(stuff) != 1 : continue
	print(stuff)
	num = float(stuff[0])
	numlist.append(num)
	j = j + 1
print('Maximum:', max(numlist))
print('Avg is :', sum(numlist)/j,',Total items are: ', j)
print('Total number of lines read are: ', i)


