import lab05_util

def print_info(serial):
	print('{} ({})'.format(restaurants[serial][0],restaurants[serial][5]))
	address= restaurants[serial][3]
	address = address.split('+')
	print('\t\t{}'.format(address[0]))
	print('\t\t{}'.format(address[1]))
	score = restaurants[serial][6]
	if len(score)<3:
		avg = sum(score)/len(score)
	else:
		avg = (sum(score)-min(score)-max(score))/(len(score)-2)
	if avg>=0 and avg<2:
		print('This restaurant is rated bad, based on {} reviews.'.format(len(score)))
	elif avg>=2 and avg<3:
		print('This restaurant is rated average, based on {} reviews.'.format(len(score)))
	elif avg>3 and avg<=4:
		print('This restaurant is rated above average, based on {} reviews.'.format(len(score)))
	else:
		print('This restaurant is rated very good, based on {} reviews.'.format(len(score)))


restaurants = lab05_util.read_yelp('yelp.txt')

serial = int(input('Please enter a valid ID => '))
if serial>0 and serial<156:
	print_info(serial-1)
else:
	print('This ID is invalid')