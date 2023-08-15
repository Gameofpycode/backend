# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
#Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18


v_detailes1={ "Color":"White"}
v_detailes2={ "Color":"White"}


print(v_detailes1["Color"])
print("enter the detailes of cars")

v_detailes1["Vehicle_name"]=input("name:")
v_detailes1["Speed"]=int(input("speed"))
v_detailes1["Mileage"]=int(input("Mileage"))

v_detailes2["Vehicle name"]=input("name:")
v_detailes2["Speed"]=int(input("speed"))
v_detailes2["Mileage"]=int(input("Mileage"))

for i in v_detailes1:
    print(v_detailes1[i])

print(v_detailes1)
print(v_detailes2)


