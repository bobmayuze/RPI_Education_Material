census = [ 340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, 5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, 8236, 17558, 17990, 18976, 19378 ]
i = len(census)
n = 1
percentage = []

while n< i:
	p = (census[n]-census[n-1])/census[n-1] * 100
	n += 1
	percentage.append(p)

ave = sum(percentage)/(i-1)

print('Average = {:.1f}%'.format(ave))