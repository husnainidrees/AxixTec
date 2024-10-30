
class Bio:

    name="Husnian"
    age=21
    city='Lahore'
    ID_Card=35202020022
    contact_no='034514582'
    father_name="idrees"
    University_name="UCP"
    degree="Bachelore"

    def f_name(self):

        # print ("my name is":{self.name})
        # print( f'Hello: {self.name}')
        return f'Hello: {self.name}'
    
    def f_age(self,age):
        print( f'Your : {age}')
        
    def f_city(self,city):
        print( f'You From : {city}')
            
    def f_degree(self,degree):
        aas= print( f' Your {degree}')
        
        return aas
    
    def f_cot(self,conta):

        print( f'Your{conta}')





        


B=Bio()
print(B.name)
print(B.age)
print(B.city)
print(B.ID_Card)
print(B.contact_no)
print(B.father_name)
print(B.degree)
print(B.University_name)


B1=Bio()

print(B1.f_name())
print(B1.f_age(age=23))
print(B1.f_city("Sialkot"))
print(B1.f_cot(conta="233333333"))
print(B1.f_degree(degree="BSCS"))
# print(B.father_name)
# print(B.degree)
# print(B.University_name)



