length = 272
data = raw_input()

def checksum(d):
	check = ''
	i = 0
	while i < len(d):
		cpl = d[i:i+2]
		i += 2

		if cpl == '00' or cpl == '11':
			check += '1'
		else:
			check += '0'

	return check


while len(data) < length:
	cpy = data[::-1]
	cpy = ''.join(['0' if x == '1' else '1' for x in cpy])
	data = data + '0' + cpy

data = data[:length]
check = checksum(data)
while len(check) % 2 == 0:
	check = checksum(check)

print check