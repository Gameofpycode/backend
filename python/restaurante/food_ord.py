


def menu(x):
    item=["eggomlet","sandwitch","dosa","pancake","eggcurry","vegmeal","fishmeal","chikenthali","coldrinks","cocktile","moktile"]
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("\n")
    print(f"--------------selecting order from <<<<  {x}  >>>>----------------")
    
    print("\n")
    print("Break-fast")
    print("food_names\tPrice\t\tDecription\n")
    br=['1) eggomlet \t40rs \tAn omlet is a dish you might order for breakfast or bunch ',
    '2) sandwitch \t80rs \tA sandwich is a food typically consisting of vegetables.',
    '3) dosa \t100rs \tA dosa is South Indian, fermented crepe made from rice batter and black lentils.',
    '4) pancake \t80rs \tA pancake cooked from butter,milk,flour and eggs.']

    for i in br:
        print(i)
    print("\n")
    print("Lunch")
    print("food_names\tPrice\t\tDecription\n")
    
    lunch=['1)eggcurry \t100rs \tEgg curry is a comforting Indian dish of curried eggs.',
            '2)vegmeal \t100rs \tA vegitables is a food typically consisting of vegetables.',
            '3)fishmeal \t200rs \tFish meal is an excellent source of highly digestible protein.',
            '4)chikenthali\t200rs\tFish meal is an excellent source of highly digestible protein.' ]
        
    for j in lunch: 
        print(j)
    print("\n")
    print("Beverages")
    print("food_names\tPrice\t\tDecription\n")
    bvg=['1)coldrinks \t80rs','2)cocktile \t120rs','3)moktile \t150rs']

    for k in bvg:
        print(k)

    ordered_item=str(input("server: select the food from menu seprated by comma:>>>"))
    list1=ordered_item.split(",")
    
    check=1
    for c in list1:
        for c1 in range(0,len(item)):
            if(c==item[c1]):
                check+=1
            else:
                check-=1
               
    
    if(check>1):
        return list1
    else:
        print("check your food name-----------------")
        return menu(x)

def bill(x,y):
    print(f"bill for {y} customers")
    total=0
    price={ "eggomlet":40,
    "sandwitch":80,
    "dosa":100,
    "pancake":80,
    "eggcurry":100,
    "vegmeal":100,
    "fishmeal":200,
    "chikenthali":200,
    "coldrinks":80,
    "cocktile":120,
    "moktile":50}
    
    for m in x:
        for i in price:
            if(m==i):
                print(f"{m}\t:{price[i]}.0Rs")
                total+=float(price[i])
    print(f"total={total}+18% GST")
    Grand_total= float(total+(total*18)/100)
    print(f"Grand total = {Grand_total}Rs")

    return Grand_total

   

    



    # print("")
    # print(item)


table1=menu("Table1")

table2=menu("Table2")
table3=menu("Table3")
print("order has been received")
print(f"customer1: ordered items from tbl1 is:{table1}")
print(f"customer2: ordered items from tbl2 is:{table2}")
print(f"customer3: ordered items from tbl3 is:{table3}")

print("************food served************")

print("customer calling waiter from table1........")

print("server: do you want anything esle, enter 'yes' if not enter 'no'")
replay_1=str(input("customer1:"))

if(replay_1=="yes"):
    table1_2nd_ordered_items=menu("table1(adding new foods)")
    for i in range (0,len(table1_2nd_ordered_items)):
        table1.append(table1_2nd_ordered_items[i])
    print(table1)

    print("server: do you want anything esle, enter 'yes' if not enter 'no'")
    replay_1=str(input("customer1:"))

    if(replay_1=="yes"):
        table1_2nd_ordered_items=" "
        table1_2nd_ordered_items=menu("table1(adding new foods)")
        for j in range (0,len(table1_2nd_ordered_items)):
            table1.append(table1_2nd_ordered_items[j])
        print(table1)
    
    else:
        counter_to_costomer1=bill(table1,"table1")
        print("\n")
        print("**************  THANK YOU  ***************")

else:
    counter_to_costomer1=bill(table1,"table1")
    print("\n")
    print("**************  THANK YOU  ***************")

print("------------------------------------------------------------------------------------------------------")

print("customer calling waiter from table2........")

print("server: do you want anything esle, enter 'yes' if not enter 'no'")
replay_2=str(input("customer2:"))

if(replay_2=="yes"):
    table2_2nd_ordered_items=menu("table2(adding new foods)")
    for k in range(0,len(table2_2nd_ordered_items)):
        table2.append(table2_2nd_ordered_items[k])
    print(table2)

    print("server: do you want anything esle, enter 'yes' if not enter 'no'")
    replay_2=str(input("customer2:"))


    if(replay_2=="yes"):
        table2_2nd_ordered_items=" "
        table2_2nd_ordered_items=menu("table2(adding new foods)")
        for l in range(0,len(table2_2nd_ordered_items)):
            table2.append(table2_2nd_ordered_items[l])
        print(table2)
    else:
        counter_to_costomer2=bill(table2,"table2")
        print("\n")
        print("**************  THANK YOU  ***************")
else:
    counter_to_costomer2=bill(table2,"table2")
    print("\n")
    print("**************  THANK YOU  ***************")

print("--------------------------------------------------------------------------------------------------")

print("customer calling waiter from table3.......")

print("server: do you want anything esle, enter 'yes' if not enter 'no'")
replay_3=str(input("customer3:"))

if(replay_3=="yes"):
    table3_2nd_ordered_items=menu("table3(adding new foods)")
    for m in range(0,len(table3_2nd_ordered_items)):
        table3.append(table3_2nd_ordered_items[m])
    print(table3)
        
    print("server: do you want anything esle, enter 'yes' if not enter 'no'")
    replay_3=str(input("customer3:"))

    if(replay_3=="yes"):
        table3_2nd_ordered_items=" "
        table3_2nd_ordered_items=menu("table3(adding new foods)")
        for n in range(0,len(table3_2nd_ordered_items)):
            table3.append(table3_2nd_ordered_items[n])
        print(table3)

    else:
        counter_to_costomer3=bill(table3,"table3")
        print("\n")
        print("**************  THANK YOU  ***************")
    
else:
    counter_to_costomer3=bill(table3,"table3")
    print("\n")
    print("**************  THANK YOU  ***************")


# counter=bill() 

