print(" hello rakesh 10 times") 
i=1
while i<=10:
    print("hello rakesh")
    i+=1


print("1 to 100")
i=1
while i<=100:
    print(i)
    i+=1

    
print("100 to 1")
i=100
while i>=1:
    print(i)
    i-=1


print("number table")
n=int(input("enter number  "))
i=1
while i<=10:
    print(n*i)
    i+=1


print("a list containing square of 1 to 10")
num=[]
i=1
while i<=10:
    num.append(i*i)
    i+=1
print(num)


print("print the element of given tuple")
num=(1,4, 9, 16, 25, 36, 49, 64, 81, 100)
idx=0
while idx<=9:
    print(num[idx])
    idx+=1


    
print(" find a element of a given tuple")
n=int(input("enter the element  "))
num=(1,4, 9, 16, 25, 36, 49, 64, 81, 100,36)
idx=0
while idx<=10:
    if(num[idx]==n):
        print("element is found at index no",idx)
    else:
        print("founding...")
    idx+=1
  


print(" sum of n  number using while loop.")
n=int(input(" enter number  "))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
    
print("  total sum =" ,sum)
        

print(" factorial  of n  number using while loop.")
n=int(input(" enter number  "))
i=1
fact=1
while i<=n:
    fact*=i
    i+=1
    
print(" factorial is=" ,fact)
        

