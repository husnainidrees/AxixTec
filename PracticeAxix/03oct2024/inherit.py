class Vehicle:

    def __init__(self,name) -> None:
        
        self.name=name

    def food(self):
        return "the food is petrol"


# super method parent k sara class sab kuch ly ly ga

class Person(Vehicle):
    
    def __init__(self,name) -> None:

        super().__init__(self,name)

    
    def food(self):
        return "the food is pasta" 
    
# polymorphism different object call ho jaty ha different foam 
class Animal:

    def __init__(self,name) -> None:
        
        self.name=name

    def food(self):
        return "the food is grass"



vh1=Vehicle('car')
per=Person('tahir')
an=Animal('pengum')


print(vh1.food)
print(per.food)
print(an.food)
print(an.food)



# ik cheez different name sy ho child ka concept inheritance k deti ha 
 
# same class ho different 