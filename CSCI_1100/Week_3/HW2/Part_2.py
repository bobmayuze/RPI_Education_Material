# Author: Yuze Bob Ma
# Date: Sept, 16th, 2016
# This code is made for CSCI-1000_HW_2_Part_1


# Define the functions we need for playing the trick.
def reverse3(three_digits_number):
	hundreds = three_digits_number // 100
	tens = three_digits_number // 10 % 10
	ones = three_digits_number % 10
	result_of_reverse3 = ones*100 + tens*10 + hundreds
	return result_of_reverse3
def reverse5(five_digits_number):
	tenthousands = five_digits_number // 10000
	thousands = five_digits_number // 1000 % 10
	hundreds = five_digits_number // 100 % 10
	tens = five_digits_number // 10 % 10
	ones = five_digits_number % 10
	result_of_reverse5 = ones*10000 + tens*1000 + hundreds*100 + thousands*10 + tenthousands
	return result_of_reverse5

# Input the 5 digit number
print('Enter a 5 digit number whose first and third digits must differ by at least 2.\nThe answer will be 1089, if your number is valid')
five_digits_number = int(input('Enter a value ==>'))
print(five_digits_number)

# Show the calculation
print('Here is the computation:')
reversed_five_digits_number = reverse5(five_digits_number)
print(five_digits_number, 'reversed is', reversed_five_digits_number)

# Get the numbers form 5 digits for substriction
first_three_digits_of_the_original_number = five_digits_number // 100
last_three_digits_of_the_reversed_number = reversed_five_digits_number % 1000
difference_between_first_three_digits_of_the_original_number_and_last_three_digits_of_the_reversed_number = abs(first_three_digits_of_the_original_number - last_three_digits_of_the_reversed_number)
print(first_three_digits_of_the_original_number, '-', last_three_digits_of_the_reversed_number, '=', difference_between_first_three_digits_of_the_original_number_and_last_three_digits_of_the_reversed_number)

# Get numbers of difference for substriction
reversed_difference_between_first_three_digits_of_the_original_number_and_last_three_digits_of_the_reversed_number = reverse3(difference_between_first_three_digits_of_the_original_number_and_last_three_digits_of_the_reversed_number)
trick_number = difference_between_first_three_digits_of_the_original_number_and_last_three_digits_of_the_reversed_number + reversed_difference_between_first_three_digits_of_the_original_number_and_last_three_digits_of_the_reversed_number
print(difference_between_first_three_digits_of_the_original_number_and_last_three_digits_of_the_reversed_number, '+', reversed_difference_between_first_three_digits_of_the_original_number_and_last_three_digits_of_the_reversed_number, '=', trick_number)

print('You see, I told you.')
