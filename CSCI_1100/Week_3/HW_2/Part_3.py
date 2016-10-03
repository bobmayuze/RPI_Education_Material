# Author: Yuze Bob Ma
# Date: Sept, 16th, 2016
# This code is made for CSCI-1000_HW_2_Part_3

# Define the function needed
def encrypt(new_string):
	new_string = new_string.replace(' a','%4%').replace('he','7!').replace('e','9(*9(').replace('y','*%$').replace('u','@@@').replace('an','-?').replace('th','!@+3').replace('o','7654').replace('9','2')
	return new_string

def decrypt(new_string):
	new_string = new_string.replace('2','9').replace('7654','o').replace('!@+3','th').replace('-?','an').replace('@@@','u').replace('*%$','y').replace('9(*9(','e').replace('7!','he').replace('%4%',' a')
	return new_string

mode = input('Enter \'E\' for encrypt or \'D\' for decrypt ==> ')
print(mode)

# Start process
if mode == 'e' or mode == 'E':
	new_string = input('Enter regular text ==> ')
	print(new_string)
	print()

	encrypted_new_string = encrypt(new_string)
	print('Encrypted as ==>',encrypted_new_string)
	difference_in_length = abs( len(new_string) - len(encrypted_new_string) )
	print('Difference in length ==>',difference_in_length)

elif mode == 'd' or mode == 'D':
	new_string = input('Enter cipher text ==> ')
	print(new_string)
	print()

	decrypted_new_string = decrypt(new_string)
	print('Deciphered as ==>',decrypted_new_string)
	difference_in_length = abs( len(new_string) - len(decrypted_new_string) )
	print('Difference in length ==>',difference_in_length)

else:
	print('I didn\'t understand ... exiting')

