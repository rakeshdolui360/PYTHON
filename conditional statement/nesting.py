# nesting means if condition unde if condition.

#driving eligibility criteria 
age=int(input("enter your age  "))
if(age>=18):
    if(age>=80):
        print("sorry you are not allowed to drive")
    else:
        print("you are eligible for driving.")
else:
    print("you are not eligible for driving.")
