

# LAMBda Function Most important

# lambda arg :expression
# string joint  sum method max ka method cube ka method b 

ls=[1,2,4,4]

letsee=lambda num: "Even" if num %2 == 0 else 'Odd'

letsee2= list(filter (lambda num:num % 2 !=0,ls))


print (letsee(5))

print(letsee2)

# advance mein list mapping aur filter b use ho jata ha  
# reduce method func2 k name sy library 
# function k ander function 
# self call kr ly us k recursion aur wo return statment mein ai 

# Magic Function dunder kya hota ha 
# jab b ik method __ underscore double k sath khatam hota ha us k hum magic function hota ha
# startign or ending mein underscore ajye abs class ka mehtod bool 
# jab b start or end  underscore mein ho jay to wo magic function hota ha

# __iter__  __next__ yeh  b magic function ha



# Class Aur Method mein difference 


# int float double->numeric

# dictionary alag data type

# Boolean Alag data type ha

# set datatype

# sequence -> data type list string tuple

                                    # Last Topic of Dictionary Basic 

Dict={
    1: "Sadd",
    2: "Husnain",
    3:"Muhammad",
}

# dictionary key value mein ata ha

print(Dict)

# empty dictionary aese ati dic{}
# list convert into dictionary

Dict2=dict([(1,"ali"),(2,"aai"),(3,"aa")])
print(Dict2)


# Nested Dictionary difficult hota ha
# Dictionary k ander dictionary availbable ha
# dictionary key pr start hoti ha index pr ni hoti ha
Dic3={ 

    1:{'first_name':"muhammad"},
    2:{'second_name':"muhammad"},
    3:{'third_name':"muhammad"},
}


# yeh nested ha is liye hum ny aese likha ha 

print(Dic3[1]['first_name'])


# ik get ka method b hota ha 
print(Dict.get(2))



# yeh kuch Method Peform krny ha
# yeh kam lazmi krna ha ap ny 

# dict.copy 
# dict.pop -> remove specifc key ko 
# dict.hashkey return true agar ha nai to false


                                        ### Operator

## floor division // result in interger 
## multiplication k liye ** 



# Json method mein stringfy use hota ha dono key value k sath 
# json can be only string where key in dictionary in hashable object 


#comparison k ander === error nai ata wo datatype check kr leta ha
# logical opertor and or not 
# bit wise operator hota ha
# ternary operator wo hota ha jo hum ik h line mein likh dete ha


# example of ternary operator
a,b=5,6
minmum="a is minimum " if a < b else "b is minimum "
print (minmum)
