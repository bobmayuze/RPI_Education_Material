sum = 0
for i in range(10):
    for j in range(10):
        sum += 1
print(sum)

sum = 0
for i in range(10):
    for j in range(i+1,10):
        sum += 1
print(sum)

sum = 0
for i in range(10):
    sum += 1
for j in range(10):
    sum += 1
print(sum)
# for num in range(2, 10):
# 	if num % 2 == 0:
# 		print("Found an even number", num)
# 		# continue
# 	print("Found a number", num)