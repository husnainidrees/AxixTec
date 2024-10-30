## OOP 

class Student:
    def __init__(self):
        self.name=""
        self.age=0
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age



if __name__=='__main__':
    student1=Student()
    student1.set_name("husnain")
    student1.set_age(23)
    print("Name:", student1.get_name())
    print("Age:", student1.get_age())