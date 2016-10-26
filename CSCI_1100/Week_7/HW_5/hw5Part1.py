# Author: Yuze Bob Ma
# Date: Oct, 17th, 2016
# This code is written for RPI_CSCI_1100 HW5 Part 1

# Import random modules for generating random number
import random

# Define the function of moving one step
def move_trainer( position, bounds, prob=0):
	'''
	position is the current (row, col) position of the trainer, passed as a tuple
	bounds is the max (rows, cols) on the grid, again as a tuple
	prob is the probability p that a pokemon will be found at the current position
	'''
	position_list = list(position)
	# position_list = [position[0],position[1]]
	direction = random.randint(0,3)
	# direction = 0
	if direction == 0:
	# Moving North
		position_list[0] -= 1
		position_list[0] = max(0, position_list[0])
	elif direction == 1:
	# Moving South
		position_list[0] += 1
		position_list[0] = min(rows-1, position_list[0])
	elif direction == 2:
	# Moving East
		position_list[1] += 1
		position_list[1] = min(cols-1, position_list[1])
	else:
	# Moving West
		position_list[1] -= 1
		position_list[1] = max(0, position_list[1])
	position = tuple(position_list)

	luck = random.random()
	num = pokemon
	if luck < prob:
		num += 1
		return (position, num)
	else:
		return (position, num)

# Input and initialize the variables
rows = int(input("Enter the integer number of rows => "))
print(rows)
cols = int(input("Enter the integer number of cols => "))
print(cols)
probability_of_finding =  float(input("Enter the probability of finding a pokemon (<= 1.0) => "))
print(probability_of_finding)
pokemon = 0

# Generating seed for random to have a same output
seed_value = 10*rows + cols
random.seed(seed_value)

row = rows//2
col = cols//2
pokemon_total = 0
position = (row, col)
bounds = (rows, cols)

# Move 250 times
for x in range(1,251):
	position,pokemon = move_trainer(position, bounds, probability_of_finding)
	# pokemon = move_trainer(position, bounds, probability_of_finding)[1]
	if x % 20 ==0:
		print("Time step {}: position {} pokemon caught since the last report {}".format(x, position, pokemon))
		pokemon_total += pokemon
		pokemon = 0

pokemon_total += pokemon
# Output the result
print("After 250 time steps the trainer ended at position {} with {} pokemon.".format(position, pokemon_total))