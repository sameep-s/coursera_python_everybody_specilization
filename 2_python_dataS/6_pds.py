#Dictonary starting
'''
purse = dict()
purse['money'] = 12
purse['Candy'] = 3
purse['Success'] = 100
print(purse)
'''

counts = dict()
names = ['csev', 'cwen', 'zqian', 'cwen']
for name in names :
	counts[name] = counts.get(name, 0) + 1


	'''#Alternate method
	if name not in counts :
		counts[name] = 1
	else :
		counts[name] = counts[name] + 1
	'''


print(counts)