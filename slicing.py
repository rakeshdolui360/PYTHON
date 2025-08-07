
str1="kalyanicollege"
ch=str1[0:8]
print(ch)
print(len(str1))
#str[0:8] and str[:8] is same
print(str1[0:8])
print(str1[:8])

#str[0:14] ,str[0:] and str[0:len(str1)] is same
print(str1[0:14])#here in str1 there is 14 character and 0 to 13 indexing .as print(str1[0:13]) means it will print "o" th index to "12" th index .so if i want to print al 0 to 13 index so i have to print(str1[0:14])
print(str1[0:len(str1)])
print(str1[0:])

print(str1[2:6])

# negative index slicing
str="apple"
print(str[-5:-2])
print(str[-5:])
print(str[:-1])
