#f.write("\n this is a next line") in a new line it  append something without truncating the file as it is opened in "a" mode.
f=open("sample3.txt","a")
f.write("\n this is a next line")
f.close()



#creating a new  text file 
f=open("sample4.txt","a")
f.close()

f=open("sample5.txt","a")
f.close()