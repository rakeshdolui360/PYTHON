

print("find 50 ")
i=1
while i<=100:
    if(i==50):
        print("50 found")
        break
    print(i)
    i+=1
    # break used to terminate loop .after break execution, loop will discontinue.
    
    
print(" find a element from a given tuple and after finding the element discontinue the loop.")
n=int(input("enter the element  "))
num=(1,4, 9, 16, 25, 36, 49, 64, 81, 100,36)
idx=0
while idx<=10:
    if(num[idx]==n):
        print("element is found at index no",idx)
        break
    else:
        print("founding...")
    idx+=1
  