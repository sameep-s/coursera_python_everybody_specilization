#Tuples
(x, y) = (4, 'ferd')
d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
print('This is the value of t: ' ,t)
print('sorted by key:')
for k, v in t:
	print(k, v)

tmp = list()
for k, v in d.items():
	tmp.append((v, k))

print('This statement prints tmp: ', tmp)
tmp = sorted(tmp, reverse=True) #reverse=true sorts from big value to small.
print('sorted by value:')
for k, v in tmp:
	print(k ,v)

