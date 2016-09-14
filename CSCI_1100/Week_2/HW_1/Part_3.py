print('Let\'s play MadLibs for Homework 1\nType one word responses to the following:')

#Assign values to variables
proper_name_1 = input('proper_name ==> ')
print(proper_name_1)
adjective_1 = input('adjective ==> ')
print(adjective_1)
noun_1 = input('noun ==> ')
print(noun_1)
verb_1 = input('verb ==> ')
print(verb_1)
noun_2 = input('noun ==> ')
print(noun_2)
emotion_1 = input('emotion ==> ')
print(emotion_1)
verb_2 = input('verb ==> ')
print(verb_2)
noun_3 = input('noun ==> ')
print(noun_3)
noun_4 = input('noun ==> ')
print(noun_4)
season = input('season ==> ')
print(season)
emotion_2 = input('emotion ==> ')
print(emotion_2)
team_name = input('team-name ==> ')
print(team_name)
adjective_2 = input('adjective ==> ')
print(adjective_2)

#Start output results
print('\n'+'Here is your Mad Lib...',end='\n\n')

print('Hello',proper_name_1+',\n'
'  ''Good morning!  Are you looking forward to a/an',adjective_1,noun_1+'?\n'
'  ''You will',verb_1,'a lot of',noun_2,'and feel',emotion_1,'when you do.\n'
'  ''If you do not, you will',verb_2,'this',noun_3+'.\n\n'
'  ''Did you watch the',noun_4,'this',season+'?\n'
'  ''Were you',emotion_2,'when the',team_name,'won?\n'
'  ''Have a/an',adjective_2,'day!')
