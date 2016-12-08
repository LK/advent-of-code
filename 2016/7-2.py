def find_abas(ip):
	retval = []
	for i in range(len(ip)-2):
		if ip[i] == ip[i+2] and ip[i+1] != ip[i]:
			retval.append(ip[i:i+3])

	return retval

line = raw_input()
count = 0
while line != '':
	openidx = line.find('[')
	abas = []
	babs = []
	while openidx != -1:
		closeidx = line.find(']')
		abas.extend(find_abas(line[:openidx]))
		babs.extend(find_abas(line[openidx+1:closeidx]))
		line = line[closeidx+1:]
		openidx = line.find('[')
	abas.extend(find_abas(line))

	for aba in abas:
		if aba[1] + aba[0] + aba[1] in babs:
			count += 1
			break

	line = raw_input()

print count