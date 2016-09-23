def hmmm( x ):
    if x[0] > x[1]:
        return (x[1], x[0])
    else:
        return x

s = ('a', 'b')
t = (1, 2, 3)
u = (4, 5, 2)
print( t[1] + u[0] )
print( t+u )
print( s[1] * t[2] )
print( hmmm(u) )
print( hmmm( (5, 2, 3) ))