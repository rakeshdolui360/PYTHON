# format of dictionaries
info={
    "name":"rakesh dolui",
    "age":20,
    "ygpa":7.4,
    "indian":True,
    "subject":["dsa","co","analog"],
    "skill":("c","html","css"),
    
   "rakesh dolui":"name",
    20 : "age",
    7.4 : "ygpa",
    True: "indian",
    ("c","html","css"):"skill"
    
}
# dictionaries store data in key:value pair. in case of key all datatypes like string, int,float,boolean  can be used but list ,tuples can not  be used as they are mutable.
# in case of value all datatypes like string, int,float,boolean and list ,tuples can be used.
# after each key:value pair , is to be given.
# duplicate keys are not allowed
print(info)
print(type(info))

# print value 
#print(info[key])
print(info["name"])
print(info[7.4])

#updation and new key: value pair assigned
info["name"]="RD"
info["state"]="west bengal"
print(info)

#empty dictionary
null_dict={}
# new key: value pair assigned in empty dictionary
null_dict["name"]="rakesh"
print(null_dict)

#nested dictionaries
student={
    "name":"rakesh dolui",
    "subjects":{
        "phy":97,
        "math":95,
        "chem":96
    },
    "age":20
}
print(student)
#print value from nested dictionaries
print(student["name"])
print(student["subjects"])
print(student["subjects"]["math"])
