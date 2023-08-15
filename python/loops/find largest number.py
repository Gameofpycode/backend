x=[4,6,8,24,12,2]
big=x[0]
for i in range (0,len(x)):
    print(x[i])
    if(big<=x[i]):
        big=x[i]
print("largest number in the giver numbers is:",big)
