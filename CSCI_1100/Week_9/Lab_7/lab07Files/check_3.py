def parse_line(line):
	if line.count('/') < 3:
		return None
	line = line.split('/')
	try:
		x = int(line[-1])
		y = int(line[-2])
		z = int(line[-3])
	except ValueError:
		return None
	j = '/'
	text = j.join(line[:-3:])
	output = (z,y,x,text)
	return(output)

def get_line(fname, parno, lineno):
	fname = str(fname) + '.txt'
	file = open(fname)
	para_count = 0
	line_count = 0
	# Go to the target paragraph
	while True:
		para_count += 1
		context = file.readline().strip()
		if context !='' :
			# para_count += 1
			while True:
				context = file.readline().strip()
				if context == '':
					break
		if context == '':
			while True:
				context = file.readline().strip()
				if context != '':
					break
		if para_count == parno-1:
			break
	# Go to the target line
	while True:
		line_count += 1
		if line_count == lineno :
			break
		context = file.readline()

	return(context)

file_num = int(input('Please enter the file number ==> '))
parno = int(input('Please enter the paragraph number ==> '))
lineno = int(input('Please enter the line number ==> '))
target_line = get_line(file_num, parno, lineno)
# target_line = get_line(1,5,4)
# file_num = 3
# parno = 87
# lineno = 7
# target_line = get_line(file_num, parno, lineno)

# print(target_line)
# data = parse_line(target_line)
# print(data)
program = ''
while True:
	target_line = get_line(file_num, parno, lineno)
	# print(target_line)
	data = parse_line(target_line)
	if data == None:
		print('ERROR!')
		break
	# print(data)
	file_num = data[0]
	parno = data[1]
	lineno = data[2]
	if data[0] == 0:
		break
	program += data[3] + '\n'
	
print(program)
output_file = open("program.py","w")
output_file.write(program)



