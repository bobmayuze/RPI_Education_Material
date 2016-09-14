# Claim Variables for calculation

# Claim the variables for calculation, the unit is mile
Jupiter_Diameter = 88846
Jupiter_To_Sun = 483632000
Earth_Diameter = 7926
Earth_To_Sun = 92957100
Sun_Diameter = 864938

# Unit is miles per second
Speed_Of_Light = 186000

# Claim value of π
π = 3.14159

# Calculation 
Sun_to_Jupiter_radius_ratio = (π*Sun_Diameter)/(π*Jupiter_Diameter)
print('Sun-to-Jupiter radius ratio:',round(Sun_to_Jupiter_radius_ratio,2) )

Sun_to_Earth_radius_ratio = (π*Sun_Diameter)/(π*Earth_Diameter)
print('Sun-to-Earth radius ratio:',round(Sun_to_Earth_radius_ratio,2) )

Jupiter_to_Earth_radius_ratio = (π*Jupiter_Diameter)/(π*Earth_Diameter)
print('Jupiter-to-Earth radius ratio:',round(Jupiter_to_Earth_radius_ratio,2) )

Jupiter_to_Earth_Sun_distance_ratio = Jupiter_To_Sun/Earth_To_Sun
print('\nJupiter-to-Earth Sun distance ratio:',round(Jupiter_to_Earth_Sun_distance_ratio,2))

Sun_to_Jupiter_volume_ratio = (4/3*π*(Sun_Diameter/2)**3)/(4/3*π*(Jupiter_Diameter/2)**3)
print('Sun-to-Jupiter volume ratio:',round(Sun_to_Jupiter_volume_ratio,2))

Sun_to_Earth_volume_ratio = (4/3*π*(Sun_Diameter/2)**3)/(4/3*π*(Earth_Diameter/2)**3)
print('Sun-to-Earth volume ratio:',round(Sun_to_Earth_volume_ratio,2))

Jupiter_to_Earth_volume_ratio = (4/3*π*(Jupiter_Diameter/2)**3)/(4/3*π*(Earth_Diameter/2)**3)
print('Jupiter-to-Earth volume ratio:',round(Jupiter_to_Earth_volume_ratio,2))

Sun_to_Earth_light_travel_time_in_minutes = Earth_To_Sun/Speed_Of_Light/60
print('\nSun to Earth light travel time in minutes:',round(Sun_to_Earth_light_travel_time_in_minutes,2))

Sun_to_Jupiter_light_travel_time_in_minutes = Jupiter_To_Sun/Speed_Of_Light/60
print('Sun to Jupiter light travel time in minutes:',round(Sun_to_Jupiter_light_travel_time_in_minutes,2))



