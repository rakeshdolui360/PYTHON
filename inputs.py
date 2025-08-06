#result for input() is always a string
name=input("enter your name:")
print("welcome",name)
print(type(name))

#input type casting
name=input("enter your name:")
age=int(input("enter your age:"))
marks=float(input("enter your marks:"))
print("welcome",name)
print("your age is",age)
print("your marks is",marks)
print(type(name))
print(type(age))
print(type(marks))
