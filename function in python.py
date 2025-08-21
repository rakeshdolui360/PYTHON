#summation 
def cal(a,b):
    sum=a+b
    print(sum)
    # return sum


cal(2,3)
cal(3,7)

#average
def cal_avg(a,b,c):
    avg=(a+b+c)/3
    print(avg)
    # return avg

cal_avg(6,8,2)

# without any parameter
def print_hello():
    print("hello")
    
    
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

#default parameter
#whenever any arguement is not given , parameter   value is taken as arguement.
def cal_prod(a=7,b=6):
    prod=(a*b)
    print(prod)

cal_prod()


def cal_prod(a,b=6):
    prod=(a*b)
    print(prod)

cal_prod(2)


#it will give error as  no value default parameter always come at first. 
# def cal_prod(a=5,b):
#     prod=(a*b)
#     print(prod)

# cal_prod(2)

def cal_prod(b,a=6):
    prod=(a*b)
    print(prod)

cal_prod(3)





    

#in built function print() len() type() range()

print("kgec")
print("rd")
print("kgec",end=" ")
print("rd")
print("kgec",end="@")
print("rd")



