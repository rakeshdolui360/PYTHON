# for loops 
#for loops are used for sequential traversing in list ,string,tuple .
list=[10,38,67,89,23,34]
for val in list:
    print(val)
    
    
str="rakesh  dolui"
for char in str:
    print(char)
    
    
    
tup=(1,2,3,6,8,"rd")
for element in tup:
    print(element)
    
    
    
#for loops with else
str="rakesh  dolui"
for char in str:
    if(char=='o'):
        print("o found")
        break
    print(char)
else:
    print("end")



#sum of n number using for loops.
n=int(input("enter number  "))
sum=0
for i in range(1,n+1):
    sum+=i
    
print("total sum is= ",sum)


#factorial  of n number using for loops.
n=int(input("enter number  "))
fact=1
for i in range(1,n+1):
    fact*=i
    
print("factorial  is= ",fact)
