
list=[]
m1=input("enter first string :")
m2=input("enter second string :")
m3=input("enter third  string:")
m4=input("enter fourth string:")
list=[m1,m2,m3,m4]
list2=list.copy()
list2.reverse()


if(list==list2):
    print("palindrome")
else:
     print(" not palindrome")



list1=[]
m11=int(input("enter first number :"))
m22=int(input("enter second number:"))
m33=int(input("enter third  number:"))
m44=int(input("enter fourth number:"))
list1=[m11,m22,m33,m44]
list3=list1.copy()
list3.reverse()


if(list1==list3):
    print("palindrome")
else:
     print(" not palindrome")

