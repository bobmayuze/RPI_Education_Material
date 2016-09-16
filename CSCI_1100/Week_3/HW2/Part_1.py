# Author: Yuze Bob Ma
# Date: Sept, 16th, 2016
# This code is made for CSCI-1000 HW 2

# import math module
import math

# Set variables used for calculation
the_amount_of_oxygen_in_the_air = 0.21
percent_of_the_oxygen_used_each_day = 0.41
number_of_days = 300

# Input value for calculations
radius_of_capsule = float(input('Radius of capsule (m) ==>'))
print(radius_of_capsule)
radius_of_oxygen_reservoir = float(input('Radius of oxygen reservoir (m) ==>'))
print(radius_of_oxygen_reservoir)
height_of_oxygen_reservoir= float(input('Height of oxygen reservoir (m) ==> '))
print(height_of_oxygen_reservoir)

# Define calculation function
def volume_sphere(radius):
	π = math.pi
	volume_of_capsule = (4/3) * π * radius ** 3
	return volume_of_capsule


volume_of_capsule = volume_sphere(radius_of_capsule)

oxygen_needed_for_the_trip = volume_of_capsule * the_amount_of_oxygen_in_the_air * percent_of_the_oxygen_used_each_day * number_of_days
print('Oxygen needed for the trip is ', round(oxygen_needed_for_the_trip,3), 'm^3', sep = '' )