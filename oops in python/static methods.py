class Student:

    # static method does not use self parameter. it work at class level.
    
    @staticmethod
    def college():
        print("kgec college")
        
    @staticmethod
    def hello():
        print("hello kgec ")


Student.college()
Student.hello()