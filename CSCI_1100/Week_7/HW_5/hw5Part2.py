# Author: Yuze Bob Ma
# Date: Oct, 17th, 2016
# This code is written for RPI_CSCI_1100 HW5 Part 2

# Import random modules for generating random number
import random

# Define functions for moving one step
def move_trainer( position, bounds, prob=0):
	'''
	position is the current (row, col) position of the trainer, passed as a tuple
	bounds is the max (rows, cols) on the grid, again as a tuple
	prob is the probability p that a pokemon will be found at the current position
	'''
	position_list = list(position)
	direction = random.randint(0,3)
	luck = random.random()
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
	elif direction == 3:
	# Moving West
		position_list[1] -= 1
		position_list[1] = max(0, position_list[1])
	position = tuple(position_list)

	num = 0
	if luck <=  prob:
		num += 1
		return (position, num)
	else:
		return (position, num)

# Define function for one stimulation
def run_one_simulation(grid = 0, probability = 0):
	'''
	runs the simulation and keeps track of the number of pokemon caught
	on each space in the grid. prob is the probability a pokemon will be caught
	at each turn
	'''
	pokemon_num = 0
	count_grid_onece = []
	position_list = position

	# Initialize the grid
	for i in range(rows):
		count_grid_onece.append( [0]*cols )
		
	for x in range(1,251):
		position_list,pokemon_num = move_trainer(position_list, bounds, probability_of_finding)
		# pokemon_num = move_trainer(position_list, bounds, probability_of_finding)[1]
		if pokemon_num == 1:
			count_grid_onece[position_list[0]][position_list[1]] += 1
		pokemon_num = 0
	return(position_list, count_grid_onece)

# Functions for finding the max and min in the grid
def find_max(target):
	collection = []
	for l in target:
		maximum = max(l)
		collection.append(maximum)
	result = max(collection)
	return(result)

def find_min(target):
	collection = []
	for l in target:
		minimum = min(l)
		collection.append(minimum)
	result = min(collection)
	return(result)

# Input and initialize the variables
rows = int(input("Enter the integer number of rows => "))
print(rows)
cols = int(input("Enter the integer number of cols => "))
print(cols)
probability_of_finding =  float(input("Enter the probability of finding a pokemon (<= 1.0) => "))
print(probability_of_finding)
num_of_stimulation = int(input('Enter the number of simulations to run => '))
print(num_of_stimulation)
print()

# Generating seed for random to have a same output
seed_value = 10*rows + cols
random.seed(seed_value)

row = rows//2
col = cols//2
position = (row, col)
bounds = (rows, cols)

count_grid = []
count_grid_total = []
count_grid_total_collection = []
for i in range(rows):
	count_grid.append( [0]*cols )
	count_grid_total.append( [0]*cols )

for y in range(0,num_of_stimulation):

	count_grid = run_one_simulation()[1]

	
	# get sum of one simulation and put the sum into a list
	sum_of_one_stumulation = 0
	for i in range(len(count_grid)):
		for p in range(len(count_grid[i])):
			sum_of_one_stumulation += count_grid[i][p]
	count_grid_total_collection.append(sum_of_one_stumulation)

	# Generating the gird of number of pokemons get at every spot
	for i in range(len(count_grid)):
		for p in range(len(count_grid[i])):
			count_grid_total[i][p] += count_grid[i][p]

# output of the grid showing the number of times that a pokemon was caught in each position.
s = ""
for i in range(len(count_grid_total)):
	for p in range(len(count_grid_total[i])):
		s += "{:4d}".format(count_grid_total[i][p])
	print(s)
	s = ""

# Output the result
Total_pokemon_caught = sum(count_grid_total_collection)
Minimum_pokemon_caught_in_simulation = [min(count_grid_total_collection), (count_grid_total_collection.index(min(count_grid_total_collection))+1)]
Maximum_pokemon_caught_in_simulation = [max(count_grid_total_collection), (count_grid_total_collection.index(max(count_grid_total_collection))+1)]
if Total_pokemon_caught != 0:
	Max_number_of_pokemon_caught_on_a_space = [find_max(count_grid_total), find_max(count_grid_total)/Total_pokemon_caught*100]
	Min_number_of_pokemon_caught_on_a_space = [find_min(count_grid_total), find_min(count_grid_total)/Total_pokemon_caught*100]

print()
print("Total pokemon caught is {}".format(Total_pokemon_caught))
print("Minimum pokemon caught was {} in simulation {}".format(Minimum_pokemon_caught_in_simulation[0], Minimum_pokemon_caught_in_simulation[1]))
print("Maximum pokemon caught was {} in simulation {}".format(Maximum_pokemon_caught_in_simulation[0], Maximum_pokemon_caught_in_simulation[1]))
if Total_pokemon_caught != 0:
	print("Max number of pokemon caught on a space is {} which was {:.2f}% of all pokemon caught".format(Max_number_of_pokemon_caught_on_a_space[0], Max_number_of_pokemon_caught_on_a_space[1]))
	print("Min number of pokemon caught on a space is {} which was {:.2f}% of all pokemon caught".format(Min_number_of_pokemon_caught_on_a_space[0], Min_number_of_pokemon_caught_on_a_space[1]))
else:
	print ('Max number of pokemon caught on a space is 0\nMin number of pokemon caught on a space is 0')
