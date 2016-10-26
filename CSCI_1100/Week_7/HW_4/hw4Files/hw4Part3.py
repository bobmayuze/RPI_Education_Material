# Author: Yuze Bob Ma
# Date: Oct, 9th, 2016
# This code is written for HW4, part 3.

# import modules
import hw4_util

# define functions

def status_position():
	print('Currently at ({}, {})'.format(position[0], position[1]))

def print_pokemon():
	print('Current pokemon:')
	i = 0
	for pokemon in pokemons:
		print('     {} at {}'.format(pokemon, locations[i]))
		i = i + 1
def move_n():
	if position[1] != 0:
		return(position[1]-1)
	else:
		return 0
def move_s():
	if position[1] != 10 :
		return(position[1]+1)
	else:
		return 10
def move_e():
	if position[0] != 10:
		return(position[0]+1)
	else:
		return 10
def move_w():
	if position[0] != 0:
		return(position[0]-1)
	else:
		return 0
# main code

# load info forom the external files
pokemons, locations = hw4_util.read_pokemon()
position = [5, 5]

print_pokemon()
print()

# Game start!
cmd = ''
turn = -1
while cmd != 'end':
	cmd = input('N,S,E,W to move, \'print\' to list, or \'end\' to stop ==> ')
	print(cmd)
	cmd = cmd.lower()

	if cmd == 'n':
		position[1] = move_n()
		status_position()
	elif cmd == 's':
		position[1] = move_s()
		status_position()
	elif cmd == 'e':
		position[0] = move_e()
		status_position()
	elif cmd == 'w':
		position[0] = move_w()
		status_position()
	elif cmd == 'print':
		print_pokemon()
		print()
		status_position()
	elif cmd == 'end':
		break
	else:
		status_position()
	turn += 1

	if (position[0],position[1]) in locations:
		position_id = locations.index((position[0],position[1]))
		print('You capture a {} on turn {}'.format(pokemons[position_id], turn))
		pokemons.remove(pokemons[position_id])
		locations.remove(locations[position_id])













