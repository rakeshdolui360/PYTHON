
def cal_sum(n):
    if(n==0):
        return 0
    return n+ cal_sum(n-1)

m=int(input("enter number "))
print(f"sum of first {m} natural  number is ",cal_sum(m))
