"""
a=3
b=3
a1="python"
b1="Python"
a2=[4,5,6]
b2=[4,8,6]

print(a is not b)
print(a1 is not b1)
print(a2 is b2)


a="Python operators"
b={1,'x',2.0,'y'}


print("P" in a)
print("p" in a)


print("python" not in a)
print(1 in b)
print('y' in b)

s="100010"
print(type(s))

c=int(s,2)
print("after coverting to int base 2:")
print(c)

e=float(8)
print("after coverting to float")
print(e)
print(type(e))



value=input("enter the value seperated by comma")

list=value.split(".")
tuple=tuple(list)
print(list)
print(tuple)

list_1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print("Before adding:: ", list_1)
list_1[2][2].append(7000)
print("After adding:: ", list_1)

list1=[1,2,4,6,8,5,90,23,56,89,12,32,2]
list1.append(9)
print(list1)
list1.count(2)
list1.extend([11,22,33])
print(list1)
print(list1.index(90))
list1.pop()
print(list1)
list1.sort()
print(list1)
list.sort(revers=True)


a={1,2,3,4,5}
b={4,5,6,7,8}
print(a-b)
print(b-a)

print(min(a))
print(max(b))"""

seta={(1,2),(1,0),(2,3)}
print(seta)
print(all({3,False}))
print(any({3,False}))
print(any({False,False}))"""











