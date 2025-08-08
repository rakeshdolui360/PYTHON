print(" please enter 4 unique number")
a=int(input("enter first number.   "))
b=int(input("enter second number.   "))
c=int(input("enter third number.   "))
d=int(input("enter fourth number.   "))
if(a>b and a>c and a>d):
    print("first number is greatest.")
elif(b>c and b>d):
    print(" second number is greatest.")
elif(c>d):
    print("third number is greatest.")
else:
    print("fourth number is greatest") 
    
    
    
