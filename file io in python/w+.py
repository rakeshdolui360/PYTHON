#f=open("sample7.txt","w+") it means we can  overwrite and read the text file.
# f.write(" this is a new line") it at first truncate all file and overwrite " this is a new line"
#nothing come as output as after overwrittng  there is nothing left to read. only change occurs in  sample7.txt file.



f=open("sample7.txt","w+")

f.write(" this is a new line")
data=f.read()
print(data)
f.close()