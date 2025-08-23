
def  fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)
    
    # return is must .otherwise it will give error.
    

print(fact(5))
print(fact(10))