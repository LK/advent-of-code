import hashlib
import re

salt = raw_input()

def gen(idx):
	return hashlib.md5(salt + str(idx)).hexdigest()

three = re.compile(r'(.)\1{2,}')
five = re.compile(r'(.)\1{4,}')

idx = 0
validation = {}
found = []
while True:
	hsh = gen(idx)
	m = five.search(hsh)
	if m != None:
		for seq in m.groups():
			seq = seq*3
			if seq in validation:
				for i in validation[seq]:
					if idx <= i + 1000:
						found.append(i)
				del validation[seq]

	m = three.search(hsh)
	if m != None:
		seq = m.group(0)[:3]
		if seq not in validation:
			validation[seq] = [idx]
		else:
			validation[seq].append(idx)

	if len(found) >= 64:
		print sorted(found)[63]
		print found
		break

	idx += 1

# lower than 15189