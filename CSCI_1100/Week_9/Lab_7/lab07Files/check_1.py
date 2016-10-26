def parse_line(line):
	if line.count('/') < 3:
		return None
	line = line.split('/')
	# if not line[-1].isdigit() and not line[-2].isdigit() and not line[-3].isdigit():
	# 	return None
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
	# return('Pass')


print(parse_line("Here is some random text, like 5/4=3./12/3/4"))




