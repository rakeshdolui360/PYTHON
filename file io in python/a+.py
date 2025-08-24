#f=open("sample8.txt","r+") it means we can  overwrite and read the text file.
# f.write(" this is a new line") it does not  truncate the  file only append " this is a new line".
# pointer start from  ending of file and append " this is a new line".
#nothing come as output as after appending there is nothing left to read. only change occurs in  sample8.txt file.



f=open("sample8.txt","a+")

f.write("\n this is a new line")
data=f.read()
print(data)
f.close()