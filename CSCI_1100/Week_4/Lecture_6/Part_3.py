# Author: Yuze Ma
# Date: Sept, 19th, 2016 
# This code is made for part 3 of lecture 
first_number = float(input('Enter the first number: '))
print(first_number)
second_number = float(input('Enter the second number: '))
print(second_number)

if first_number > 10 and second_number > 10:
	print('Both are above 10.')
elif first_number <= 10 and second_number <= 10:
	print('Both are below 10.')

print('Average is',round((first_number + second_number)/2,2))
