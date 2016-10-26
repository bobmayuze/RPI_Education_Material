import lab05_util
import sys
import webbrowser 

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

def load_info(serial):
	address= restaurants[serial][3]
	address = address.split('+')
	return(address[0], address[1])

restaurants = lab05_util.read_yelp('yelp.txt')

serial = int(input('Please enter a valid ID => '))
if serial>0 and serial<156:
	print_info(serial-1)
else:
	print('This ID is invalid')

info_address = load_info(serial-1)
location_url = 'http://www.google.com/maps/place/{},{}'.format(info_address[0], info_address[1])
direction_url = 'http://www.google.com/maps/dir/110 8th Street Troy NY/{},{}'.format(info_address[0], info_address[1])


print('What would you like to do next?')
print('1. Visit the homepage')
print('2. Show on Google Maps')
print('3. Show directions to this restaurant')
user_input = int(input('Your choice (1-3)? ==> '))
if user_input == 1:
	webbrowser.open('http://xkcd.com/1319/')
elif user_input == 2:
	webbrowser.open(location_url)
elif user_input == 3:
	webbrowser.open(direction_url)
else:
	sys.exit()
