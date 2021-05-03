print("value =", 10+20+30+40+50)
print("010","1234","5678", sep="-")
print("value=", end=", ")
print("value=", 20)

print("a=", format(3.14159, "8.3f"))
print("b =", format(10000,"10d"))
print("c=", format(125000,"3,d"))

name="James"
age=35
price=125.456
print("name: %s, age:%d, data=%.2f" %(name, age, price))

print("name: {}, age: {}, data={}". format(name,age,price))
print("name: {1}, age: {0}, data={2}". format(age,name,price))

uid=input("id input: ")
query = f"select*from member where uid={uid}"
print(query)