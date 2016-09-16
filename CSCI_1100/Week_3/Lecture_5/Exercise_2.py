# Author: Yzue Bob Ma
# Date Sept, 15th, 2016
# This code is made for Lecture 5, exercise 2.

# Define the function
def frame_string(String):
	Number_Of_Asterik = len(String)
	print('***','*'*Number_Of_Asterik,'***', sep='')
	print('**',String,'**')
	print('***','*'*Number_Of_Asterik,'***', sep='')

# Output results
frame_string('Spanish Inquisition')
print()
frame_string('Ni')