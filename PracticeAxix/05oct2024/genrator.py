

# Yeh Sir k Code Ha

#  yeh Generetor k concept ha 
def fibona():
    a,b =0,1
    yield a
    a,b=b, a+b


gen =fibona()


#  for k indr yeh _ anomyous ha 
# bady bady dataset k yield kiya jata ha
# dataset k memory mein load kiye begair kr sakty ha

# generator quick response deta ha 
for _ in range(10):
    # next k keyword sy kam mein ly kr aty ha hum 
    print(next(gen))






# Generator ik iteratble object hota jo iteerable oject k lazily iterate krta ha 
#  Generator k automatically generate kiya ja sakta ha

# Genertor memory efficient hota ha
# Generator jo ha wo yield keyword use hota ha






def cube_generator(n):
    for i in range(1,n+1):
        yield i ** 3



n = int(input("Enter a Number To Check The Cube"))

cube=cube_generator(n)


print("The Cube Number is ",n)

for num in cube:
    print(num)






############################################## Code Second ############################333

# Random Number Print Krna 

import random

def range_func(start,end):

    while True:

        yield random.randint(start,end)
    




start=int(input("Enter a Number To Start"))

end =int(input("Enter a End Number"))



random_number=range_func(start,end)


# yeh range 10 jo ha wo sirf jo user values dy ga us mein jo 10 random number genreate kr dy ga

for _ in range(10):
    print(next(random_number))