import lab05_util

def print_info(serial):
	print('{} ({})'.format(restaurants[serial][0],restaurants[serial][5]))
	address= restaurants[serial][3]
	address = address.split('+')
	print('\t\t{}'.format(address[0]))
	print('\t\t{}'.format(address[1]))
	score = restaurants[serial][6]
	avg = sum(score)/len(score)
	print('Average Score: {:.2f}'.format(avg))

restaurants = lab05_util.read_yelp('yelp.txt')
i = 0

while i<4:
	print_info(i)
	i += 1