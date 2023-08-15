employee_details={}
sallary=int(input("enter sallary amount:"))

if(sallary>=65000):
    emp_details={"designation":"manager"}
    x=sallary/10
    ba=sallary-x
    hr=float(x*0.5)
    t=float(x*0.32)
    d=float(x*0.18)

    emp_details["Basic price"]=ba
    emp_details["HRA"]=hr
    emp_details["TA"]=t
    emp_details["DA"]=d


    print(emp_details)
elif(sallary>=50000 and sallary<65000):
    emp2_details={"designation":"TL"}
    x = sallary / 10
    ba = sallary - x
    hr = float(x * 0.5)
    t = float(x * 0.32)
    d = float(x * 0.18)

    emp2_details["Basic price"] = ba
    emp2_details["HRA"] = hr
    emp2_details["TA"] = t
    emp2_details["DA"] = d

    print(emp2_details)
elif(sallary >=35000 and sallary<50000):
    emp3_details = {"designation": "Developer"}
    x = sallary / 10
    ba = sallary - x
    hr = float(x * 0.5)
    t = float(x * 0.32)
    d = float(x * 0.18)

    emp3_details["Basic price"] = ba
    emp3_details["HRA"] = hr
    emp3_details["TA"] = t
    emp3_details["DA"] = d

    print(emp3_details)
elif (sallary >= 20000 and sallary <35000):
    emp4_details = {"designation": "tester"}
    x = sallary / 10
    ba = sallary - x
    hr = float(x * 0.5)
    t = float(x * 0.32)
    d = float(x * 0.18)

    emp4_details["Basic price"] = ba
    emp4_details["HRA"] = hr
    emp4_details["TA"] = t
    emp4_details["DA"] = d

    print(emp4_details)
else:
    print("sallary must be above 20000")