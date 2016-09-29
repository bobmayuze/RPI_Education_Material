# Author: Yuze Bob Ma
# Date: Sept, 29th, 2016

values = [ 14, 10, 8, 19, 7, 13 ]
num_1 = int(input('Enter a value: '))
print(num_1)
values.append(num_1)

num_2 = int(input('Enter another value: '))
print(num_2)
values.insert(2,num_2)

print(values[3],values[-1])

diff = max(values)-min(values)
ave = sum(values)/len(values)
values.sort()
if len(values)//2 == 1:
	middle = values[len(values)//2]
else:
	middle = (values[len(values)//2] + values[len(values)//2-1])/2

print('Difference:', diff)
print('Average: {:.1f}'.format(ave))
print('Median:', middle)
