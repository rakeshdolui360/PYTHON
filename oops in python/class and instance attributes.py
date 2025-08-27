
class student:
    # class attribute
    college_name="kgec"
    name="anonymus"
    
    def __init__(self,name,marks):
        # object attribute
        self.name=name
        self.marks=marks
    
s1=student("rakesh",95)
print(s1.name)
print(s1.marks)
s2=student("ruhi",86)
print(s2.name)
print(s2.marks)


print(s1.college_name)
print(s2.college_name)

#object attribute has more priority than class attribute
print(s1.name)
        