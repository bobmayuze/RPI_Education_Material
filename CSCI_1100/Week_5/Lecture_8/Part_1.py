l1 = [ 6, 12, 13, 'hello' ]
print(l1[1], l1[-2])
l1.append( 15 )
print( len(l1) )
print( len(l1[3]) )
l1.pop(3)
l1.sort()
l1.insert(2, [14, 15] )
l1[3] += l1[4]
l1[3] += l1[2][1]
print(l1[3])
l1.pop()
l1[2].remove(14)
print(l1)