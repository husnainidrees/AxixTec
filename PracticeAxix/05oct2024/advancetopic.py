

# context manger setup or tear kr sakty ho with k keyword k sath 
# context manager



class Context_Manager():

    def __init__(self):

        print('init Method Called')
    
    def __enter__(self):
        print("enter Method Called")
        return self
    
    def __exit__(self,exc_type,exc_value,exc_tracback):

        print("exit method called")
    

with Context_Manager() as manager:
    print("With Statement Block")









class FileManager():
     def __init__(self,filename,mode):
         self.filename=filename
         self.mode=mode

     def __enter__(self):
         self.file=open(self.filename,self.mode)
         return self.file
     def __exit__(self,exc_type,exc_val,exc_tb):
         self.file.close()





with FileManager('test.txt' , 'w') as f:
    f.write('Waseem \n')
    f.write('Ali ')
    
    


# control krti ha class k execution k liye 
# type sy inherit kiya ha 


class Meta(type):

    def __new__(cls,name,base,attribute):
        if 'my_attribute' not in attribute:

            # raise exception handiling k liye use hota ha

            raise AttributeError('Class must defing "my_attribute" ')
        return super().__new__(cls,name,base,attribute)
    



#  jis tara inherit krty ha is tara yeh kam ha
class newClas(metaclass=Meta):

    my_attribute=42




print(newClas().my_attribute)




# agar koi issue ata to yeh raise krta ha exception 
# khudi h new class create kry gy





#  Async Behaviour

