import math

Radius_1 = 5
Radius_2 = 32

Area_1 = round(math.pi * pow(Radius_1,2), 2)
print('Area 1 =',Area_1)

Area_2 = math.pi * Radius_2 ** 2
Out_String = 'Area 2 = {:.2f}'.format(Area_2)
print(Out_String)