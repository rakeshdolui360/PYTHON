
class student:
    # if we don't create any parameterized constructor then python automatically create default constructor .
    # default constructor
    # def __init__(self):
    #     pass
    # parameterized constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
s1=student("rakesh",98)
print(s1.name)
print(s1.marks)

s2=student("rosi",95)
print(s2.name)
print(s2.marks)


  

        
