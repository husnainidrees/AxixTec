

# stand alone function kam nai kry jab tak call ni kro gy waapis ni kry ga

def myfucn():
    lst2=[5,4,5,2]
    lst3=['x','y','z']

    #yeh new cheez ha mere liye 
    # dict.fromkeys()
    # ap k remove kr k dy deta ha
    res=list(dict.fromkeys(lst2))

    lst2.reverse()
    
    return lst2



## SLicing 

# lst2[:: -1]

# Filteration Method 
# filter ik number leta ha
# filter ik builtin function ha
# custom filter b lagty ha
# memory mein bilkul jaga ni leta ha memory efficent ha 

def myfiltere(num):
    if num%2==0:
        return num
    

def myf():
    ls=[32,54,23,2,80]
    res=list(filter(myfiltere,ls))
    res1=[num for num in ls  if num>10]
    return res

# ik operator ha concise way ha for loop ka  
# memory efficent or cashier k code pr kam kr rhy ha
# list Compresenion 

# Mpping difficult concept samjhta ha


def xby2(num):
    return num*2

# mapping  ik function ik list dictionary 
# filter mapping k concept pr kam krta h 
# yeh kam is k sath ho jay is liye hum mapping use krty ha

lt=[2,4,5,5,]
xby2oflst=list(map(xby2,lt))



## Two list k Combine krna 
## jab hum k paring combine list in the form of Tuple
## combine the two coordinate points in x and y 

l9=[1,4,5,7,8,8]
l0=[10,55,4,55,33,332]

lst_combine=list(zip(l0,l9))




#  Question poocha jata ha  most frequent elemnt in the list
# COllection mein counter ka method ha
# most frequent elemnt or descending wise chalta ha
# max ik parameter datatype accept or key accept krta ha 

# koi number list mein exist krta ha ya nai to use in method

mostFreq=max(set(l9),key=l9.count)

#2D List
ls2D=[[1,4],
      [5,6],
      [7,8]]

# flatten ka method numpy ha yaha pr hum kese use kry gy 
lst_r=[num for each_lst in ls2D for 
       num in each_lst]
# yeh tariqa ha flattene krny ka 
# phir return krwa dy gy 
 


#### List k Characterist mutable order duplicate b accept krta ha
##    begin ny end [:] append use hota ha item change index pr ja kr 
# ik sy zaida remove krna ha to del use krty ha
# append end pr dalta h
# insert kisi b index pr krta ha 
# extend list k end pr add krta ha iterable 

# jo b list ha us k item b aur jo ap add krny cha rhy ha wo b add kr deta ha end pr 
# item of list or iterable item are added at the end of list

# clear ka method all clear kr deta ha
# count lena ho specific 
#copy method achi bat ha shallow copy 
# shallow copy refernce nai ata
# agar list ajy to wo deep copy hota ha kyu k refernce ajata ha


# yeh example ha 
list=[3,4,5]
lst=[6,7,8]

list.extend(lst)



