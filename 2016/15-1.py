discs = [[10, 13], [15, 17], [17, 19], [1, 7], [0, 5], [1, 3]]
#discs = [[4, 5], [1, 2]]

i = 0
while True:
	good = True
	for j in range(len(discs)):
		if (discs[j][0] + i + j + 1)%discs[j][1] != 0:
			good = False

	if good:
		break

	i += 1

print i