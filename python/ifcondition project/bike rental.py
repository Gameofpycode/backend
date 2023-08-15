#bike rental
print("rent for two wheeler = 100rs/hr\t\t\t rent for Four wheeler =180rs/hr")
vehicle_type=int(input("enter the vehical type=>2wl or 4wl:"))
rent_for_two_wheeler=100
rent_for_four_wheeler=180

hours=int(input("enter the how many hours required:"))

if(2== vehicle_type):
    if(hours>=1):
        paying_am = hours * rent_for_two_wheeler
        gst18 = (paying_am * 18) / 100
        print("total rent amount is:\t", paying_am)
        print("gst18%=", gst18)
        total = paying_am + gst18
        print("Amount to be pay=>", paying_am, "+18%gst")
        print("total amount fot rent is:", total)
    else:
        print("min one hour is mondatory")

elif(4==vehicle_type):
    if (hours >= 1):
        paying_am = hours * rent_for_two_wheeler
        gst18 = (paying_am * 18) / 100
        print("total rent amount is:\t", paying_am)
        print("gst18%=", gst18)
        total = paying_am + gst18
        print("Amount to be pay=>", paying_am, "+18%gst")
        print("total amount fot rent is:", total)
    else:
        print("min one hour is mondatory")

