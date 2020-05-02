
fh = open('mbox-short.txt')
for line in fh:
	if not line.startswith('From s'): continue
	print(line.rstrip())
	words = line.split()
	email = words[1]
	print(email)
	pieces = email.split('@')
	print(pieces[1])
	print('\n')
	print('hoe ass nigga.')
