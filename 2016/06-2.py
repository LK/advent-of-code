data = [{}, {}, {}, {}, {}, {}, {}, {}]

line = raw_input()
while line != '':
	for i in range(8):
		if line[i] in data[i]:
			data[i][line[i]] += 1
		else:
			data[i][line[i]] = 1
	line = raw_input()

print data