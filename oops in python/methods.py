class student:
    
    college_name="kgec"
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def welcome(self):
        print("welcome",self.name)
        
    def get_marks(self):
        print(f"hi {self.name} you got {self.marks} marks.")
        
s1=student("rakesh",95)
print(s1.name)
print(s1.marks)
s2=student("ruhi",86)
print(s2.name)
print(s2.marks)

s1.welcome()
s2.get_marks()
        
