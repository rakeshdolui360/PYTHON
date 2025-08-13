#format
set1={1,2.0,"rakesh",True,(1,2,"rd")}
#set mutable. but element of set unique and immutable. so int,float,string,boolean,tuples can  be element of set. but list and dict can not be element of set.
print(set1)
print(type(set1))

#unordered print return. if element is repeated then set ignore the duplicate element while printing.
set1={1,2,2.3,"rakesh",True ,(1,2,"rd"),4,4,2,2.3,"rakesh"}
print(set1)
set1={1,2,2.0,"rakesh",True,(1,2,"rd"),4,4,2,2.0,"rakesh",3}
print(set1)

#empty dict
set2={}
print(type(set2))
#empty set format 
set3=set()
print(type(set3))
