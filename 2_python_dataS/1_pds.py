fruit = 'bananna'
if 'nn' in fruit:
	print('Found it!!!!') 

F = fruit.upper()
print(F)
#print(dir(fruit))

nstr = fruit.replace('bananna', 'Apple')
print(nstr)
print(fruit.startswith('bananna'))


#Important code for slicing out strings, low level though.
data ="asckmcsmcpmcpdsocmdspoc@uct:ac:za asdasdsadsdsd "
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
host = data[atpos+1 : sppos]
print(host)
print(len('banana') * 7)

#Code to count number of a's.
word = 'banana'
count = 0
for letter in word:
	if letter == 'a' :
		count = count + 1
print(count)