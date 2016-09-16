# Author: Yzue Bob Ma
# Date Sept, 15th, 2016
# This code is made for Lecture 5, exercise 1.

# Define the function
def convert2fahren(Celsius_Temperature):
	Fahrenheit_Temperature = Celsius_Temperature*9/5 + 32
	return Fahrenheit_Temperature

# Output the results by calling the function
Temp = convert2fahren(0)
print('0 ->',Temp)
Temp = convert2fahren(32)
print('32 ->',Temp)
Temp = convert2fahren(100)
print('100 ->',Temp)