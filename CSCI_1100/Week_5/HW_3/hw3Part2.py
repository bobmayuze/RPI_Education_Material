# Author: Yuze Bob Ma
# Date: Sept, 30th, 2016
# This code is write for RPI CSCI 1100 course, HW 3 part 2

# Import modules for use and load file
import hw3_util
import sys


# Define functions

def make_1x1():
	from_1x1 = legos.count('1x1')
	total = from_1x1 
	print('I can make {} 1x1 pieces:'.format(total))
	print('     0 pieces of 1x1 using 2x4 pieces.')
	print('     0 pieces of 1x1 using 2x2 pieces.')
	print('     0 pieces of 1x1 using 2x1 pieces.')
	print('     {} pieces of 1x1 using 1x1 pieces.'.format(from_1x1))

def make_2x1():
	from_1x1 = int(legos.count('1x1')/2)
	from_2X1 = legos.count('2x1')
	total = from_1x1 + from_2X1
	print('I can make {} 2x1 pieces:'.format(total))
	print('     0 pieces of 2x1 using 2x4 pieces.')
	print('     0 pieces of 2x1 using 2x2 pieces.')
	print('     {} pieces of 2x1 using 2x1 pieces.'.format(from_2X1))
	print('     {} pieces of 2x1 using 1x1 pieces.'.format(from_1x1))

def make_2x2():
	from_1x1 = int(legos.count('1x1')/4)
	from_2X1 = int(legos.count('2x1')/2)
	from_2x2 = legos.count('2x2')
	total = from_1x1 + from_2X1 + from_2x2
	print('I can make {} 2x2 pieces:'.format(total))
	print('     0 pieces of 2x2 using 2x4 pieces.')
	print('     {} pieces of 2x2 using 2x2 pieces.'.format(from_2x2))
	print('     {} pieces of 2x2 using 2x1 pieces.'.format(from_2X1))
	print('     {} pieces of 2x2 using 1x1 pieces.'.format(from_1x1))

def make_2x4():
	from_1x1 = int(legos.count('1x1')/8)
	from_2X1 = int(legos.count('2x1')/4)
	from_2x2 = int(legos.count('2x2')/2)
	from_2x4 = legos.count('2x4')
	total = from_1x1 + from_2X1 + from_2x2 + from_2x4
	print('I can make {} 2x4 pieces:'.format(total))
	print('     {} pieces of 2x4 using 2x4 pieces.'.format(from_2x4))
	print('     {} pieces of 2x4 using 2x2 pieces.'.format(from_2x2))
	print('     {} pieces of 2x4 using 2x1 pieces.'.format(from_2X1))
	print('     {} pieces of 2x4 using 1x1 pieces.'.format(from_1x1))

# Input
legos = hw3_util.read_legos('legos.txt')
target = input('What type of lego do you need? ==> ')
print(target)
print()

if target == '1x1':
	make_1x1()
elif target== '2x1':
	make_2x1()
elif target== '2x2':
	make_2x2()
elif target== '2x4':
	make_2x4()
else:
	print('Illegal lego')
	sys.exit()
