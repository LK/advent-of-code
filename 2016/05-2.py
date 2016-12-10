import hashlib
doorid = raw_input()

password = [None] * 8
done = 0
i = 0
while done < 8:
	hash = hashlib.md5(doorid + str(i)).hexdigest()
	if hash[:5] == '00000':
		try:
			pos = int(hash[5], 10)
			if pos < 8:
				if password[pos] == None:
					password[pos] = hash[6]
					done += 1
		except:
			pass
	i += 1

print password