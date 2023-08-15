user_name= input("enter the user name:")
password=int(input("enetr the password:"))
account_bal=102500

user_name1 = "sachin"
password1=1402

if(user_name == user_name1):
    if(password == password1):
        print("account balace is :",account_bal)
        print("selct option below:\n\n")
        print("for widthdraw enetr 1\t\t\tfor close the process enter 2")
        select1=1
        select2=2
        select=int(input(">"))

        if(select1 == select):

            pin1="0010"
            pin=str(input("enter pin number:"))
            if (pin1 == pin):
                w_amount = int(input("Please enter withdrawal amount:"))
                account_bal = account_bal - w_amount
                print("account balace is :",account_bal)
                print("Thank You")
        else:
            print("Thank you")

    else:
        print("password did't match")
else:
    print("user name not avilable")


