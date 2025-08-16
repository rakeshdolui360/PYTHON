
nullset=set()
#set.add(element)
nullset.add(2)
nullset.add(3)
nullset.add(4.0)
nullset.add(2)
nullset.add("rakesh dolui")
nullset.add((2,3,5,"rd"))

print(nullset)

#set.remove(element)
nullset.remove(2)
print(nullset)



#set.pop()
#random poping element
print(nullset.pop())


set1={1,2,3}
set2={2,3,4}

#set1.union(set2)   combines both set value and returns new set of unique element.
print(set1.union(set2))

#set1.intersection(set2)    combines common value and returns new set.
print(set1.intersection(set2))


# set.clear() clear all elements
nullset.clear()
print(nullset)
