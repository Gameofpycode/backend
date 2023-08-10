a={1,2,3.6,5,7.8,'r','s'}
b={2,5,'d','abc','r'}
c={'m',2,23,76,4.7,'r','s'}


print("set of U b=",a.union(b))

print("set a U B U c U=",a.union(b,c))


print(a&b)
print(a&b&c)
