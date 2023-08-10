first_name=('anil','saraha','mehth','naven')
last_name=('narang','smith','raj','kumar')


ages=(49,55,39,33)

res=zip(first_name,last_name,ages)

print(res)

customers=tuple(res)

print(customers)


first_name,last_name,ages=customers[2]
print(first_name,ages,"years old")
