# Author: Yuze Bob Ma
# Date: Oct, 9th, 2016
# This code is written for HW4, part 2.

# import modules
import hw4_util
import sys


# load the files for the list
area_1 = input('Enter the first area to check => ')
print(area_1)
cdata1 = hw4_util.read_deaths(area_1)
if cdata1 == []:
	print(area_1 + ' is an invalid name')
	sys.exit()
area_2 = input('Enter the second area to check => ')
print(area_2)
cdata2 = hw4_util.read_deaths(area_2)
if cdata2 == []:
	print(area_2 + ' is an invalid name')
	sys.exit()

# analyse the trend
trend = []
for i in range(11):
	diff = cdata1[i] - cdata2[i]
	if abs(diff) <= 50:
		trend.append('=')
	elif diff < -50:
		trend.append('+')
	else:
		trend.append('-')
area_1_tendency = trend.count('+')
area_2_tendency = trend.count('-')
if area_1_tendency > area_2_tendency:
	tendency = 'I would rather live in {} than {}'.format(area_1, area_2)
elif area_1_tendency < area_2_tendency:
	tendency = 'I would rather live in {} than {}'.format(area_2, area_1)
else:
	tendency = ('{} and {} are the same'.format(area_1, area_2))

# Inverse the trend and organize them into a string
trend_inverse = trend[::-1]
trend_format = ''.join(trend_inverse)

# Output the results
print()
print(' '*7 + '2013' + ' '*3 + '2003')
print('Trend: ' + trend_format)
print()
print(tendency)