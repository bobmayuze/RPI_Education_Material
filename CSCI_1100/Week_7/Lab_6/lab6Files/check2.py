def ok_to_add(row, col, num):
	num = str(num)
	# Check if the num is in the row
	if num in bd[row]:
		print('This number cannot be added')
		return False 
	# Check if the num is in the col
	for x in range(0,9):
		if num == bd[x][col]:
			print('This number cannot be added')
			return False 
	# Check if the num is in the 3x3 block
	# Area 1
	if 0<=row<=2 and 0<=col<=2:
		for i in range(0,3):
			for p in range(0,3):
				if num == bd[i][p]:
					print('This number cannot be added')
					return False 
	# Area 2				
	if 3<=row<=5 and 0<=col<=2:
		for i in range(3,6):
			for p in range(0,3):
				if num == bd[i][p]:
					print('This number cannot be added')
					return False 
	# Area 3				
	if 6<=row<=8 and 0<=col<=2:
		for i in range(6,9):
			for p in range(0,3):
				if num == bd[i][p]:
					print('This number cannot be added')
					return False 
	# Area 4				
	if 0<=row<=2 and 3<=col<=5:
		for i in range(0,3):
			for p in range(3,6):
				if num == bd[i][p]:
					print('This number cannot be added')
					return False 
	# Area 5				
	if 3<=row<=5 and 3<=col<=5:
		for i in range(3,6):
			for p in range(3,6):
				if num == bd[i][p]:
					print('This number cannot be added')
					return False 
	# Area 6				
	if 6<=row<=8 and 3<=col<=5:
		for i in range(6,9):
			for p in range(3,6):
				if num == bd[i][p]:
					print('This number cannot be added')
					return False
	# Area 7				
	if 0<=row<=2 and 6<=col<=8:
		for i in range(0,3):
			for p in range(6,9):
				if num == bd[i][p]:
					print('This number cannot be added')
					return False
	# Area 8				
	if 3<=row<=5 and 6<=col<=8:
		for i in range(3,6):
			for p in range(6,9):
				if num == bd[i][p]:
					print('This number cannot be added')
					return False
	# Area 9				
	if 6<=row<=8 and 6<=col<=8:
		for i in range(6,9):
			for p in range(6,9):
				if num == bd[i][p]:
					print('This number cannot be added')
					return False
	bd[row][col] = num
	return True    

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

# print(len(bd))
# print(len(bd[0]))
# print(bd[0][0])
# print(bd[8][8])
print("------------------------")
s = ""
for i in range(len(bd)):
	for p in range(len(bd[i])):
		s += "{:2}".format(bd[i][p])
		if p == 2 or p ==5:
			s += "| "
	if i == 3 or i == 6:
		print("------------------------")
	s = "|{}|".format(s)

	print(s)
	s = ""
print("------------------------")


row_user = int(input('Please type the row'))
col_user = int(input('Please type the col'))
number_user = int(input('Please type the number'))
ok_to_add(row_user,col_user,number_user)

print("------------------------")
s = ""
for i in range(len(bd)):
	for p in range(len(bd[i])):
		s += "{:2}".format(bd[i][p])
		if p == 2 or p ==5:
			s += "| "
	if i == 3 or i == 6:
		print("------------------------")
	s = "|{}|".format(s)

	print(s)
	s = ""
print("------------------------")
