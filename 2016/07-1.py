def check_abba(ip):
	for i in range(len(ip)-3):
		if ip[i] == ip[i+3] and ip[i+1] == ip[i+2] and ip[i+1] != ip[i]:
			return True

	return False

line = raw_input()
count = 0
while line != '':
	good = []
	bad = []
	openidx = line.find('[')
	while openidx != -1:
		closeidx = line.find(']')
		good.append(line[:openidx])
		bad.append(line[openidx+1:closeidx])
		line = line[closeidx+1:]
		openidx = line.find('[')
	good.append(line)

	correct = False
	for good_ in good:
		if check_abba(good_):
			correct = True
			break

	for bad_ in bad:
		if check_abba(bad_):
			correct = False
			break

	if correct:
		count += 1

	line = raw_input()

print count