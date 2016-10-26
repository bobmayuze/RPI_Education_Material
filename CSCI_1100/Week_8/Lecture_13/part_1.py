f = open("census_data.txt")
line1 = f.readline()
line1 = line1.strip()
# line2 = f.read()
line3 = f.readline().strip()
print(line1)
# print(line2)
if line3 == '':
	print(line3)
	# print('===')
# f.close()
# f = open("census_data.txt")
# s = f.read()
# line_list = s.split('\n')
# print(len(line_list))
# line_list = s.strip().split('\n')
# print(len(line_list))
# def fff():
# 	return True

# if not fff():
# 	print('fffffff')