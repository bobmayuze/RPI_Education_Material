# Author: Yuze Bob Ma
# Date: Sept, 30th, 2016
# This code is write for RPI CSCI 1100 course, HW 3 part 2

# Import modules for use and load file
import hw3_util
import sys
legos = hw3_util.read_legos('legos.txt')

# Define functions
def judge(target):
	if target in legos:
		return 0
	else:
		print('Illegal lego')
		sys.exit()

def make_1x1():
	from_1x1 = legos.count('1x1')
	total = from_1x1 
	print('I can make {} 1x1 pieces:'.format(total))
	print('\t0 pieces of 2x4 using 2x4 pieces.')
	print('\t0 pieces of 2x4 using 2x2 pieces.')
	print('\t0 pieces of 2x4 using 2x1 pieces.')
	print('\t{} pieces of 2x4 using 1x1 pieces.'.format(from_1x1))

def make_2x1():
	from_1x1 = int(legos.count('1x1')/2)
	from_2X1 = legos.count('2x1')
	total = from_1x1 + from_2X1
	print('I can make {} 2x1 pieces:'.format(total))
	print('\t0 pieces of 2x4 using 2x4 pieces.')
	print('\t0 pieces of 2x4 using 2x2 pieces.')
	print('\t{} pieces of 2x4 using 2x1 pieces.'.format(from_2X1))
	print('\t{} pieces of 2x4 using 1x1 pieces.'.format(from_1x1))

def make_2x2():
	from_1x1 = int(legos.count('1x1')/4)
	from_2X1 = int(legos.count('2x1')/2)
	from_2x2 = legos.count('2x2')
	total = from_1x1 + from_2X1 + from_2x2
	print('I can make {} 2x2 pieces:'.format(total))
	print('\t0 pieces of 2x4 using 2x4 pieces.')
	print('\t{} pieces of 2x4 using 2x2 pieces.'.format(from_2x2))
	print('\t{} pieces of 2x4 using 2x1 pieces.'.format(from_2X1))
	print('\t{} pieces of 2x4 using 1x1 pieces.'.format(from_1x1))

def make_2x4():
	from_1x1 = int(legos.count('1x1')/8)
	from_2X1 = int(legos.count('2x1')/4)
	from_2x2 = int(legos.count('2x2')/2)
	from_2x4 = legos.count('2x4')
	total = from_1x1 + from_2X1 + from_2x2 + from_2x4
	print('I can make {} 2x4 pieces:'.format(total))
	print('\t{} pieces of 2x4 using 2x4 pieces.'.format(from_2x4))
	print('\t{} pieces of 2x4 using 2x2 pieces.'.format(from_2x2))
	print('\t{} pieces of 2x4 using 2x1 pieces.'.format(from_2X1))
	print('\t{} pieces of 2x4 using 1x1 pieces.'.format(from_1x1))

# Input
target = input('What type of lego do you need? ==> ')
print(target)
print()
judge(target)
if target == '1x1':
	make_1x1()
elif target== '2x1':
	make_2x1()
elif target== '2x2':
	make_2x2()
else:
	make_2x4()
