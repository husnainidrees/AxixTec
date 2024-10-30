

# # decorator yeh basiccally function kisi aur function 
# # k behaviour k modify krta ha login k ander use krty ha
# # access k control kiya jata login mein use kiya jata ha 
# # library use k jati ha Time builtin ha


####################################### Sir ny JO Code Krwaya tha hum k wo yeh ha ###################################

# import time

# def timer_decorator(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         resu= func(*args,**kwargs)
#         end_time=time.time()

#         # Magic Method ha YEh
#         print(f"Func{func.__name__} took {end_time-start_time:.4f} seconds")
#         return resu
#     # yeh wrapper return kry ga
#     return wrapper





# @timer_decorator
# def slow_fun(sec):
#     time.sleep(sec)
#     return 'Done'



# print('Execution ')
# print(slow_fun(3))








# #############################################        2 Code For Practice ##########################################


# def  decorator(func):
#     def wrapper(*args,**kwargs):
#         # yeh tariqa hota ha function aur us k argument k call 
#         # is k hum magic function b khaty ha

#         print(f"calling {func.__name__} with args: {args}, with key argumetn {kwargs} ")

#         # call the orignal function

#         res=func(*args,**kwargs)

#         print( f"{func.__name__} returned {res}")

#         return res
    
#     return wrapper



# @decorator

# def multiply(x,y):
#     return x*y




# result=multiply(10,20)

# print(result)



    ####################### print the Cache   3 Code For Practice ########################################



def cache_retrive(func):

    cach={}

    def wrapper(*args,**kwargs):
        key= (*args,*kwargs.items())

        if key in cach:
            print("Result From Cashe ")
            return cach[key]
        
        result=func(*args,**kwargs)
        cach[key]=result

        return result
    
    return wrapper





@cache_retrive
def calculte(x,y):
    print("Calculate The Two Product Number ")
    return x*y




# Call the decorated function multiple times
print(calculte(4, 5))  # Calculation is performed
print(calculte(4, 5))  # Result is retrieved from cache
print(calculte(5, 7))  # Calculation is performed
print(calculte(5, 7))  # Result is retrieved from cache
print(calculte(-3, 7))  # Calculation is performed
print(calculte(-3, 7))  # Result is retrieved from cache