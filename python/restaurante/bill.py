def bill(x):
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

    print("\n")
    print("**************  THANK YOU  ***************")

v=["dosa","pancake","vegmeal"]

y=bill(v)