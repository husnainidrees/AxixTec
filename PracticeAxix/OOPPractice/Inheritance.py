
# ALL Inhertance concept clear 

class Vehicle:
    def __init__(self):
        # __ private k liye use hota ha
        self.__brand=""
        self.__model=""
        self.__age=0
    
    def set_brand(self,brand):
        self.__brand=brand

    def set_model(self,model):
        self.__model=model

    def set_age(self,age):
        self.__age=age
    
    # get lazmi self leta ha
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_age(self):
        return self.__age
    
    def display_info(self):
       
        return f"Brand: {self.__brand}, Model: {self.__model}, Year: {self.__age}"



class Car(Vehicle):
    def __init__(self):
        # yani k parent class k sab kuch ly liya 
        super().__init__()  # Calling the base class constructor
        self.__mileage = 0

    # Setter for mileage
    def set_mileage(self, mileage):
        self.__mileage = mileage

    # Getter for mileage
    def get_mileage(self):
        return self.__mileage

    # Overriding the display_info method to include mileage
    def display_info(self):
        vehicle_info=super().display_info()  # Call base class method

        return f"{vehicle_info}, Mileage: {self.__mileage} km/l"

if __name__=='__main__':

    vehice1=Car()
    vehice1.set_brand("Honda")
    vehice1.set_model("civic")
    vehice1.set_age(2023)
    vehice1.set_mileage(15)

    print(vehice1.display_info())

    