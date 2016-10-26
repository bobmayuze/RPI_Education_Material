# values=[-10, 20, 5.2, -57, 3, -9, 81, 7, 6, 4, -3]
# for value in values:
#     if value < 0:
#         continue
#     if abs(value) > 50:
#         break
#     print(value)

# def a(w, s, z):
# 	w *= 2
# 	s *= 2
# 	for l in range(len(z)):
# 		z[l] *= 2
# 	print(w)
# 	print(s)
# 	print(z) 
# i=7
# j = "Prestige"
# k = list(range(5))
# a(i, j, k)
# print(i)
# print(j)
# print(k)

# def is_earlier(t1, t2):
# 	if t1[1]<t2[1]:
# 		return -1
# 	elif t1[1]>t2[1]:
# 		return 1
# 	else:
# 		if t1[0]==t2[0]:
# 			return 0
# 		elif t1[0] == 12:
# 			return -1
# 		elif t2[0] == 12:
# 			return 1
# 		elif t1[0] < t2[0]:
# 			return -1
# 		elif t1[0] > t2[0]:
# 			return 1
# print(is_earlier((5,'PM'), (5,'AM')))

# import random 
# def run_turtle(N):
# 	step = 0
# 	p = N/2
# 	d = -1
# 	while True:
# 		step += 1
		
# 		luck = random.random()
# 		# luck = 0.5
# 		if luck < 0.4:
# 			d = -d
# 			if d > 0:
# 				p += 1
# 			else:
# 				p -= 1
# 		else:
# 			if d > 0:
# 				p += 1
# 			else:
# 				p -= 1
# 		print(p)
# 		if p == N or p == -1:
# 			break
# 	if p>0:
# 		end = 'right'
# 	else:
# 		end = 'left'
# 	return(step-1, end)
# print(run_turtle(10))

# def is_on_diagonal(bd, row, col, word):
# 	if row + len(word) > len(bd) or col + len(word) > len(bd[0]):
# 		return False
# 	word_l = list(word)
# 	for i in range(len(word_l)):
# 		if bd[row][col] == word_l[i]:
# 			row += 1
# 			col += 1
# 		else:
# 			return False
# 	return True


# bd = [
# ['c', 'i', 'w', 'i', 'z', 'z', 'e', 'k', 's', 'm'],
# ['g', 't', 'u', 'p', 'e', 'i', 'p', 'r', 'f', 'j'],
# ['e', 'n', 'j', 'p', 'd', 't', 'b', 'f', 'd', 'r'],
# ['m', 'e', 'r', 'k', 'v', 'x', 'e', 's', 'u', 'd'],
# ['r', 'm', 'k', 's', 'q', 'j', 'q', 'l', 'p', 'r'],
# ['d', 'j', 'x', 'f', 'p', 'o', 's', 'm', 'w', 'a'],
# ['c', 'k', 'c', 'b', 'i', 'a', 'h', 'x', 'm', 'm'],
# ['d', 'r', 'l', 's', 'k', 't', 'm', 'e', 'a', 'n'],
# ['h', 'i', 'j', 's', 'd', 't', 'z', 'i', 'y', 'j'],
# ['g', 'f', 'k', 'f', 'h', 'p', 'w', 'f', 'u', 'h']]


# print(is_on_diagonal(bd, 3, 7, 'spam'))

def all_ok(input_line, N):
	grades = input_line.split(',')
	grades_clean = []
	# print(len(grades))
	if len(grades) != N:
		return False
	for i in range(len(grades)):
		grades_clean.append(int(grades[i].strip()))
	for i in range(N):
		if grades_clean[i] < 0 or grades_clean[i] > 100:
			return False
	return True


f = open('file.txt')
N = int(f.readline())
for line in f:
	if not all_ok(line, N):
		print(line.strip())






