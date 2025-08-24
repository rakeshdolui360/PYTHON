#f.write("this is a new line") it at first truncate the file .then it overwrite the file by "this is a new line".
# nothing come as output. only change occurs in  sample2.txt file.

f=open("sample2.txt","w")
f.write("this is a new line")
f.close()
