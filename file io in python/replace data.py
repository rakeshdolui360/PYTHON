
with open("sample12.txt","r") as f:
    data=f.read()
    new_data=data.replace("e","o")
    print(new_data)
with open("sample12.txt","w") as f:
    f.write(new_data) 