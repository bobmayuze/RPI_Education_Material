# import sys

# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input('Plz enter ur word, sir ==> ')
# word_l = list(word)
# length = len(word_l)
# print(word_l)

# # i = 1
# # for charater in range(length-1):
# # 	if not word_l[i] < word_l[i+2]:
# # 		print('Game over')
# # 		sys.exit()
# # 	i += 2
# # 	if i > length-2:
# # 		break

# i = 0
# for charater in range(length-1):
# 	if word_l[i] not in vowels:
# 		print('The word \'{}\' is not alternating'.format(word))
# 		sys.exit()
# 	i += 1
# 	if word_l[i] in vowels:
# 		print('The word \'{}\' is not alternating'.format(word))
# 		sys.exit()
# 	i += 1
# 	if length % 2 == 0:
# 		if i > length-1:
# 			break
# 	else:
# 		if i > length-2:
# 			break

# print('LOL')

# haha = 10
# def add_one_second():
# 	return(haha + 1)
	

# haha = add_one_second()
# print(haha)

def read_pokemon():
    turns = []
    pokemon = []
    pos = []
    y = []
    for line in open('pokemon.txt'):
        m = line.strip().split()
        turns.append(int(m[0]))
        pokemon.append(m[1])
        pos.append((int(m[2]), int(m[3])))
    return pokemon, pos     

print(read_pokemon()[0])
print(read_pokemon()[1])



