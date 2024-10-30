
class Animal:
    # normal method or class k method k classify krta ha self 
    # phaly attribute hoty ha
    # self sirf constructor k sath use hot ha
    # magic method string str k represent
    # init constructor bana kr deta h
    # __str__ ha wo 

    # Access modifier 
    #  # access modifier private public protected  aphi child k liye hota ha sirf  
    # protected
    # private 

    # ik _underscore protected 
    # double underscre private ban jata ha 

   # phir hum aese use kry gy  self.__name 

    _name=None
    _age=None

    arg1="Dog"
    arg2="Cat"

    # is k bad methods hoty ha

    def func(self):
        print('Hello')

    def __str__(self) -> str:
        return f"the name is {self.name}"
    
    
    # is k hum setter khaty ha
    def setName(self,new_name):
        self.name=new_name
    
    # getter
    def getName(self):

        return self.name
    
    # behaviour ka method
    def behaviour(self):
        pass

    #food k method
   

    







# object aese banta ha
Ani=Animal()
print (Ani.arg1)

print(Ani.func())

# none is liye ata k return kuch nai kr rha 

# information extract krni ha 






# constructor k liye init banaty ha 
# jab tak construct na ho to wo faida ni ho ga


def __init__(self,name,age,region)->None:
    self.name=name
    self.age=age
    self.region=region

def getDetail(self):
    return f"The name is {self.name} and age is {self.age} and region is
    {self.region}" 



# object
# animal k class lakin 

anm=Animal(name="crow",age=2,regi="pakistan")
anm1=Animal(name="dog",age=23,regi="sea")
anm2=Animal(name="cat",age=22,regi="s")

print(anm.getDetail())





########################################################################

        #Inheritance ka Concept ############################


