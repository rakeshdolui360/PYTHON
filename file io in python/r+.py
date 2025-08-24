#f=open("sample6.txt","r+") it means we can  overwrite and read the text file.
# f.write(" this is a new line") it does not  truncate the  file only overwrite " this is a new line".
# pointer start from  starting of file and overwrite " this is a new line".this change happen in file only and  then pointer stay at the end of "e" 
# after that data=f.read() only read after "e" and print the remaining.

f=open("sample6.txt","r+")

f.write(" this is a new line")
data=f.read()
print(data)
f.close()