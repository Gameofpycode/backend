num=int(input("enter the number:"))
flag=num
rev=0
while(num>0):
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
    print(num)
print("reverse of the number is :",rev)

if(flag==rev):
    print(" given number is palindrome")
else:
    print("given number is not a palindrome")
