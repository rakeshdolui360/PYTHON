#format
tup=(2,3,25,17,25)
print(tup)

#like string concatenation
tup1=(235,28,28,27)
tup2=tup+tup1
print(tup2)
print(type(tup2))

#length of tuples
print(len(tup))

#indexing in tuples
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])


# in tuples we can store element of different types
tup3=("rakesh",20,"male")
print(tup3)

# updating element
# in tuples we can access element but can not update it
# tup=(2,3,25,17,25)
# tup[3]=4
# print(tup)

#empty tuple
tup4=()
print(tup4)
print(type(tup4))

# one element tuple format end , mandatory or it will work as integer,float,string not as tuples.
tup5=(5,)
print(tup5)

tup6=(7)
#  it's  treated as integer .not as tuples
print(tup6)
print(type(tup6))

tup7=(7.0)
#  it's  treated as float .not as tuples
print(tup7)
print(type(tup7))

tup8=("rakesh")
#  it's  treated as string .not as tuples
print(tup8)
print(type(tup8))

# tup=(2,3,25,17,25)
# tup=(2,3,25,17,25,) both same


