string = ''
for i in range(0,9):
	string += str(i)+' '
print(string)

rows = 9
cols = 9
grid = []

for y in range(rows):
	grid.append([0]*cols)



for y in range(rows):
	for x in range(cols):
		grid[y][x] = "{},{}".format(y,x)
		# print("{},{}".format(y,x))

s = ""
for i in range(len(grid)):
	for p in range(len(grid[i])):
		s += "{:4}".format(grid[i][p])
		if p == 2 or p ==5:
			s += " "
	if i ==2 or i == 5:
		s += "\n"
	print(s)
	s = ""

