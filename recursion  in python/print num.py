# print 100 to 1
def num(n):
    if(n==0):
        return
    print(n)
    num(n-1)

num(100)

# print 1 to 100
def num(n):
    if(n==101):
        return
    print(n)
    num(n+1)

num(1)

# odd print
print("odd numer between 1 to 100")
def num(n):
    if(n==101):
        return
    elif(n%2!=0):
        print(n)
    num(n+1)
    
num(1)

# even print
print("even number between 1 to 100")
def num(n):
    if(n==101):
        return
    elif(n%2==0):
        
        print(n)
    num(n+1)
    
num(1)

    
        
        