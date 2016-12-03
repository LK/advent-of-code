line = raw_input()
count = 0
while line != '':
	nums = [int(num) for num in line.split(' ') if num != '']
	if 2 * max(nums) - sum(nums) < 0:
		count += 1
	line = raw_input()

print str(count)