# Author: Yuze Bob Ma
# Date: Sept, 16th, 2016
# This code is made for CSCI-1000_HW_2_Part_1

# import math module
import math

# Set variables used for calculation
the_amount_of_oxygen_in_the_air = 0.21
percent_of_the_oxygen_used_each_day = 0.41
number_of_days = 300
π = math.pi


# Input value for calculations
radius_of_capsule = float(input('Radius of capsule (m) ==> '))
print(radius_of_capsule)
radius_of_oxygen_reservoir = float(input('Radius of oxygen reservoir (m) ==> '))
print(radius_of_oxygen_reservoir)
height_of_oxygen_reservoir= float(input('Height of oxygen reservoir (m) ==> '))
print(height_of_oxygen_reservoir)

# Define calculation function
def volume_sphere(radius):
	volume_of_capsule = (4/3) * π * radius ** 3
	return volume_of_capsule

def volume_cylinder(radius, height):
	volume_of_cylinder = π * radius ** 2 * height 
	return volume_of_cylinder


# Calculation
volume_of_capsule = volume_sphere(radius_of_capsule)
volume_of_cylinder = volume_cylinder(radius_of_oxygen_reservoir,height_of_oxygen_reservoir)
oxygen_needed_for_the_trip = volume_of_capsule * the_amount_of_oxygen_in_the_air * percent_of_the_oxygen_used_each_day * number_of_days
amount_of_oxygen_the_cylinder_holds = 210 * volume_of_cylinder
number_of_tanks = math.ceil(oxygen_needed_for_the_trip/amount_of_oxygen_the_cylinder_holds)

# Output the results
print()
print('Oxygen needed for the trip is {:.3f}m^3.'.format(oxygen_needed_for_the_trip) )
print('Each cylinder holds {:.3f}m^3 at 3000 psi.'.format(amount_of_oxygen_the_cylinder_holds))
print('The trip will require', number_of_tanks, 'reservoir tanks.')







