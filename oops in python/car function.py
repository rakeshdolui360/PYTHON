
# abstraction
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    
    def start(self):
        self.acc=True
        self.brk=True
        self.clutch=True
        print("car started...")
    
car1=car()
car1.start()




class car:
    def __init__(self):
        self.acc=True
        self.brk=True
        self.clutch=True
    
    def stop(self):
        self.acc=False
        self.brk=False
        self.clutch=False
        print("car stopped...")
    

car2=car()
car2.stop()
    