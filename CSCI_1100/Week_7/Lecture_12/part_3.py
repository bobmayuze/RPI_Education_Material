def find_min(target):
	collection = []
	for l in target:
		minimum = min(l)
		collection.append(minimum)

	result = min(collection)
	return(result)

v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
print("Min of list v: {}".format(find_min(v)) )
u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], [ 'rain', 'snow', 'sun' ] ]
print("Min of list u: {}".format(find_min(u)) )