
str="i am a coder and a programmer"

# str.endswith("substr") returns true if string ends with substr otherwise it returns false.
print(str.endswith("er"))
print(str.endswith("oer"))


# str.capitalize() capitalizes 1st character of string.
print(str.capitalize())
print(str)# str.capitalize() does not change in main string.it creates new string.
str1=str.capitalize()
print(str1)#now str.capitalize() can change in main string.


# str.replace("old","new") it replaces new value at the place of old value .
print(str.replace("a","o"))
print(str.replace("coder","programmer"))

#str.find("") returns 1st index of 1st occurrer
print(str.find("o"))
print(str.find("a"))
print(str.find("coder"))
print(str.find("t"))#if nothing  is found then it returns -1


# str.count("substr") count the occurance of substr.
print(str.count("a"))
print(str.count("am"))
print(str.count("er"))

str1=input("enter a string ")
print(" occurane of 'o' in this str is", str1.count("o"))