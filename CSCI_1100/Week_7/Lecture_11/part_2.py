Dale_h = int(input('Enter Dale\'s height: '))
print(Dale_h)
Erin_h = int(input('Enter Erin\'s height: '))
print(Erin_h)
Sam_h = int(input('Enter Sam\'s height: '))
print(Sam_h)


kids_tuples = [
        ('Dale', Dale_h),
        ('Erin', Erin_h),
        ('Sam', Sam_h),
]

result = sorted(kids_tuples, key=lambda kids: kids[1], reverse = True)
for s in result:
	print(s[0])