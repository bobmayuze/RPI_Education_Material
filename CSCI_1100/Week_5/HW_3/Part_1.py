# Author: Yuze Bob Ma
# Date: Sept, 30th, 2016
# This code is write for RPI CSCI 1100 course, HW 3 part 1

# import moudles
import read_names
import sys

# Define functions for sympalize the analytics
def analyse_female(target_female, year):
	(female_names,female_counts) = read_names.top_in_year(year, 'f')
	if female_names != []:
		if target_female in female_names: 
			target_female_index = female_names.index(target_female)
			rank = target_female_index + 1
			counts = female_counts[target_female_index]
			percentage_to_top = female_counts[target_female_index]/female_counts[0]*100
			percentage_to_sum = female_counts[target_female_index]/sum(female_counts[0:250])*100
			print('\t{0}:{1:3d} {2:5d} {3:7.3f} {4:7.3f}'.format(year, rank, counts, percentage_to_top, percentage_to_sum))
		else:
			print('\t{0}: Not in the top 250'.format(year))
	else:
		return 0

def analyse_male(target_male, year):
	(male_names,male_counts) = read_names.top_in_year(year, 'f')
	if male_names != []:
		if target_male in male_names: 
			target_male_index = male_names.index(target_male)
			rank = target_male_index + 1
			counts = male_counts[target_male_index]
			percentage_to_top = male_counts[target_male_index]/male_counts[0]*100
			percentage_to_sum = male_counts[target_male_index]/sum(male_counts[0:250])*100
			print('\t{0}:{1:3d} {2:5d} {3:7.3f} {4:7.3f}'.format(year, rank, counts, percentage_to_top, percentage_to_sum))
		else:
			print('\t{0}: Not in the top 250'.format(year))
	else:
		return 0
# Load the data into the module
read_names.read_from_file("top_names_1880_to_2014.txt")
# Input values
year = int(input('Enter the year to check => '))
print(year)
if year < 1880 or year > 2014:
	print('Year must be at least 1880 and at most 2014')
	sys.exit()

target_female = input('Enter a female name => ')
print(target_female)
print('Data about female names')
print(target_female+':')
analyse_female(target_female, year-10)
analyse_female(target_female, year-5)
analyse_female(target_female, year)
analyse_female(target_female, year+5)
analyse_female(target_female, year+10)
print()

target_male = input('Enter a male name => ')
print(target_male)
print('Data about male names')
print(target_male+':')
analyse_male(target_male, year-10)
analyse_male(target_male, year-5)
analyse_male(target_male, year)
analyse_male(target_male, year+5)
analyse_male(target_male, year+10)