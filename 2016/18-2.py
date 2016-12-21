rows = [raw_input()]

for i in range(399999):
	row = ''
	prev = '.' + rows[-1] + '.'
	for j in range(len(rows[0])):
		if prev[j:j+3] == '^^.':
			row += '^'
		elif prev[j:j+3] == '.^^':
			row += '^'
		elif prev[j:j+3] == '^..':
			row += '^'
		elif prev[j:j+3] == '..^':
			row += '^'
		else:
			row += '.'

	rows.append(row)
		
print sum([r.count('.') for r in rows])