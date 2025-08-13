
student={
    "name":"rakesh dolui",
    "subjects":{
        "phy":97,
        "math":95,
        "chem":96
    },
    "age":20
}

#student.keys()

print(student.keys())
#dict_keys(['name', 'subjects', 'age'])
print(list(student.keys()))
#['name', 'subjects', 'age']

print(len(student))
print(len(list(student.keys())))




#student.values()

print(student.values())
# dict_values(['rakesh dolui', {'phy': 97, 'math': 95, 'chem': 96}, 20])
print(list(student.values()))
# ['rakesh dolui', {'phy': 97, 'math': 95, 'chem': 96}, 20]




#student.items()

print(student.items())
# dict_items([('name', 'rakesh dolui'), ('subjects', {'phy': 97, 'math': 95, 'chem': 96}), ('age', 20)])
print(list(student.items()))
# [('name', 'rakesh dolui'), ('subjects', {'phy': 97, 'math': 95, 'chem': 96}), ('age', 20)]




#student.update({key:value})

student.update({"city":"kolkata"})
print(student)
student["state"]="west bengal"
print(student)





#student.get(key)

print(student.get("age"))
print(student["age"])

print(student.get("age2"))
#  for invalid keys  print(student.get("age2")) returns none.
print(student["age2"])
#  for invalid keys print(student["age2"]) gives error.thats why it is not used in large project.