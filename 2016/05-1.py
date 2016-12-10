import hashlib
doorid = raw_input()

password = ''
i = 0
while len(password) < 8:
	hash = hashlib.md5(doorid + str(i)).hexdigest()
	if hash[:5] == '00000':
		password += hash[5]
	i += 1

print password