# Author: Yuze Ma
# Date: Sept, 19th, 2016
# This code is made for Lab 3, Checkpoint 2

def process_result():
	country = input('Please type in the country:')
	num_wins = int(input('Please type in num_wins: '))
	num_draw = int(input('Please type in num_draw: '))
	num_losses = int(input('Please type in num_losses: '))
	goals_for = int(input('Please type in goals_for: '))
	goals_against = int(input('Please type in goals_against: '))

	points = num_wins * 3+num_draw
	goal_adv = goals_for - goals_against

	print(country)
	print("Win:", num_wins, "Lose:", num_losses, "Draw:", num_draw)
	print("Total number of points:", points, "Goal advantage:", goal_adv)

process_result()