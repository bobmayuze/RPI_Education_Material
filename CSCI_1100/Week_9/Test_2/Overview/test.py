

# 1
# def compare_date(L1, L2):
# 	if L1[1] < L2[1]:
# 		return -1
# 	elif L1[1] > L2[1]:
# 		return 1
# 	else:
# 		if L1[0] < L2[0]:
# 			return -1
# 		elif L1[0] > L2[0]:
# 			return 1
# 		else:
# 			return 0


# print(compare_date([10,1995], [8,1995]))
# print(compare_date([5,2010], [5,2010]))
# print(compare_date([10,1993], [8,1998]))

# 2
# v = [7,3,5,1,10,6]
# v = [7]
# v = []
# if len(v)>1:
# 	h_1 = max(v)
# 	v.remove(h_1)
# 	h_2 = max(v)

# 	print(h_2, h_1)

# elif len(v) == 1:
# 	print(v[0])

# else:
# 	print()

# 3

# restaurants = [	[ 'Acme', 'Italian', 2, 4, 3, 5],
# 				[ 'Flintstone', 'Steak', 5, 2, 4, 3, 3, 4],
# 				[ 'Bella Troy', 'Italian', 1, 4, 5] ]


# for i in range(len(restaurants)):
# 	if restaurants[i][1] != "Italian":
# 		continue
# 	if 1 in restaurants[i]:
# 		continue
# 	print(restaurants[i])


# 4
# in_file = open('yelp.txt')
# high = []
# for line in in_file:
# 	# p_line = parse_line(line)
# 	print(line)
# 	if p_line[5] > 4:
# 		high.append(p_line[0])


# 5
# def chess_score(history):
# 	P = history.count('P')
# 	B = history.count('B')
# 	K = history.count('K')
# 	R = history.count('R')
# 	Q = history.count('Q')
# 	total = P * 1 + B * 3 + K * 3 + R * 5 + Q * 9
# 	return total
# print(chess_score('BQBP'))
# chess_score('PB')

# 6 
# data = [ [2, 5, 7],
# 		[3, 6, 10],
# 		[1, 2, -3 ],
# 		[2, 4, 1]]
# sum_1 = []
# sum_2 = []
# sum_3 = []
# for i in range(len(data)):
# 	sum_1.append(data[i][0])
# 	sum_2.append(data[i][1])
# 	sum_3.append(data[i][2])
# print(sum(sum_1))
# print(sum(sum_2))
# print(sum(sum_3))

# 7

# l1 = []
# # for i in range(100,-1,-1):
# # for i in range(55,-3,-2):
# # for i in range(3,31,2):
# for i in range(-95,95,5):
# 	l1.append(i)
# print(l1)

# 8
# result = []
# v = [ 10, 12, 3, -5, 5, 6 ]
# # v = [ 0, 10, 3, 6, 5, 1 ]
# item = 0
# i = 0
# while item >= 0:
# 	item = v[i]
# 	result.append(item)
# 	i += 1
# 	print(item)
# result.pop()
# print(sum(result))

# 9 
# v = [ 17, -5, 15, -3, 12, -5, 0, 12, 22, -1 ]
# v_new = []
# for i in range(len(v)):
# 	if v[i] > 0:
# 		v_new.append(v[i])
# v_new.sort()
# # print(v_new[::-1])
# for i in range(len(v_new)):
# 	print(v_new[i])

# 10
# mylist = [1,4,8,12,6]
# x = mylist.sort()
# print(x)
# mylist = [1,4,8,12,6]
# slice1 = mylist[2:4]
# slice1[0] = 20
# print(slice1)
# print(mylist)

# 11
# for i in range(len(v)):
# 	if v[i] > 0 :
# 		print(v[i])

# 12
# def spam(a1,b1,a2,b2):
# 	if (a1 == a2) and (b1 > b2):
# 		return 1
# 	else:
# 		return 0
# def egg(a1,b1,a2,b2):
# 	if (a1 > a2) and (b1 == b2):
# 		return 0
# 	else:
# 		return 1

# a1 = 3
# b1 = 4
# a2 = 6
# b2 = 4
# print(spam(a2, b2, a1, b1))
# print(egg(a1, b1, a2, b2))

# c = spam(a1, b2, a2, b1)
# print(c)
# c += egg(a1, b2, a2, b1)
# print(c)

# 13
# input_file = open('in.txt')
# output_file = open('out.txt','w')
# context = []
# for line in input_file:
# 	# print(line)
# 	context.append(line.replace('\n',''))
# for i in range(0,len(context),2):
# 	print('{}'.format(context[i]))
# 	output_file.write('{}\n'.format(context[i]))
# 	i += 1

# 14
# input_file = open('test2.txt')
# context = []
# p = []
# n = []
# for line in input_file:
# 	context.append(line.strip())
# context.remove('')
# for i in range(len(context)):
# 	if int(context[i]) > 0:
# 		p.append(int(context[i]))
# 	elif int(context[i]) < 0:
# 		n.append(int(context[i]))
# 	else:
# 		continue
# print(context)
# print(p)
# print(n)

# 15
# i=4
# L = [ 0, 12, 3, 5, 2, -1 ] 
# while 0 <= i and i < len(L):
# 	if L[i] < 0:
# 		break
# 	else:
# 		i = L[i]
# 	print(i, L[i])

# tough = 2
# for i in range(2):
# 	s=1
# 	for j in range(i, tough):
# 		s += tough
# 	print (s)
# 	print (tough)
# 	tough = s
# print (tough)

# 16
# def get_min(v):
# 	v.sort()
# 	return v[0]

# def get_max(v):
# 	x = max(v)
# 	return x

# v = [ 14, 19, 4, 5, 12, 8 ]
# if len(v) > 10 and get_min(v) > 6:
# 	print("Hello")
# 	print(v[0])
# 	print(v[4])
# else:
# 	print("So long")
# 	print(v[0])
# 	print(v[-1])
# 	if len(v) < 10 or get_max(v):
# 		print(get_max(v))
# 		print(v[0])
# 		print(get_min(v))
# 		print(v[0])

# 17

# def elephant(height):
# 	time_step = 1
# 	steps = 0
# 	while steps < height:
# 		steps += time_step
# 		steps -= time_step//3
# 		time_step += 1
# 	print("{}, {}".format(time_step, steps))
# elephant(0)
# elephant(5)
# elephant(6)

# 18
# def remove_something(z):
# 	z.remove(z[z[0]])

# v = [ 1, 8, [12, 8], 'hello', 'car' ]
# x = 'salad'
# if len(v[2]) >= 2:
# 	if x > v[3]:
# 		print ('One')
# 		if v[0] == 1:
# 			print('Three')
# 	else:
# 		print('Two')
# elif len(v) == 5:
# 	print('Six')
# else:
# 	v.append('five')
# 	print ('Ten')
   
# remove_something(v)
# print(v[1])
# print(v[2])
# v.append(x)
# print(len(v))

# 19
# x = [[1,2,3,4],[4,3,2,1],[2,1,4,2],[2,1,4,5]]
# s = ''
# for i in range(len(x)):
# 	for p in range(len(x[i])):
# 		if p == 2:
# 			s += '| '
# 		s += str(x[i][p])+ ' '
# 	if i == 2:
# 		print('----|----')
# 	print(s)
# 	s = ''

# 20
# cmd = ''
# collection = []
# result = 0
# positive = 0
# while cmd != 'stop':
# 	cmd = input('Enter a value ==> ')
# 	collection.append(cmd)
# collection.pop()
# for i in range(len(collection)):
# 	result += float(collection[i])
# 	if float(collection[i]) > 0:
# 		positive += 1

# print(result, positive)

# 21
# def remove_val(l, num):
# 	while True:
# 		if num in l:
# 			l.remove(num)
# 			continue
# 		break
# x = [1, 4, 2, 1, 2, 4, 4, 2, 5, 5, 2]
# remove_val(x,4)
# print(x)

# 22
# a1 = [11,8,11,9]
# a2 = [11,9,8,12]

# a2_competitions = []
# s = ''

# for i in range(len(a1)):
# 	if a2[i]>a1[i]  :
# 		a2_competitions.append(str(i+1))
# if a2_competitions == []:
# 	print('A2 sucks')
# else:
# 	for i in a2_competitions:
# 		s += i+ ' '
# 	print('A2 is', s)

# 23
# L1 = ['cat', 'dog', 'hawk', 'tiger', 'parrot']
# print(L1[1:-1])
# print(L1[1:-2])
# print(L1[1:-4])
# print(L1[1:0])
# print(L1[1:10])
# print(L1[::-1])
# print(L1[1:4:2])
# print(L1[::-2])


#24
# a = 25
# b = 11
# while True:
# 	print(a, b)
# 	if a <= 0 or b <= 0:
# 		break 
# 	if a > b:
# 		a=a-b 
# 	else:
# 		b=b-a 
# 	b -= 1
# 	a += 1

mylist = [10, -5, 4, 8, 1000, -1, -120, 18, 5.2]
for item in mylist:
    if item < 0:
        continue
print(item)
# def spam(l,s):
# 	m = len(s)/2
# 	s1 = s[:m]
# 	s2 = s[m:]
# 	if l.count(s1) == 0:
# 		l.append(s1)
# 	if l.count(s2) == 0:
# 		l.append(s2)
# l = ['ab','cd','de','fg']
# s1 = 'abcde'
# s2 = 'fghi'
# spam(l,s1)
# print(s1)
# print (l)
# l = spam(l,s2)
# print(s2)
# print(l)





