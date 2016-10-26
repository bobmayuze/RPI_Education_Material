chain = []
p = 1
while p != 0:
	i = int(input('Enter a value (0 to end): '))
	print(i)
	chain.append(i)
	p = i

chain.remove(0)
minimum = min(chain)
maximum = max(chain)
avg = sum(chain)/len(chain)
	
print("Min: {}".format(minimum))
print("Max: {}".format(maximum))
print("Avg: {:.1f}".format(avg))

