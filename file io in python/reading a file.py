# comment out others and run one  code  .



# 1
# data=f.read() it reads entire file.

f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()



#2
# after reading all file, pointer is at end so nothing left for f.readline() .that's why it give empty space line  for each f.readline() function.

f=open("sample.txt","r")
data=f.read()
print(data)
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
f.close()



#3
# data=f.read(8) it reads only 8 chracter.
# after that   one line and one empty space line( due to \n)for each case(print(line1),print(line2)) is print from sample.txt 
# and in case of print(line3), as there is no 3rd line in sample.txt so it will print empty space line.

f=open("sample.txt","r")
data=f.read(8)
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)

f.close()

