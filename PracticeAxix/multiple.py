
# Factorial of two Number

# def factorai(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorai(n-1)


# if __name__=='__main__':

#     num=int(input("Enter a number "))
#     res=factorai(num)
#     print("Factorial of This Number is : " , res)



###############################################################

                        # Compound Interest Rate
# A=P(1+r/100)t

# def compound(pri,rate,time):
#     interes=pri*((1+rate/100)**time)
#     return interes

# princi=int(input("Enter a Number: "))
# inter=float(input("Enter Interest Value: "))
# tim=float(input("Enter the Duraaion: "))


# result=compound(princi,inter,tim)

# print("The Interest Amount is:",result)


#######################################################

                        # Generate The Sentences

# subject=["I" , "Love"]
# verb=["Play","You"]
# object=["Hockey","Football"]

# for i in range(len(subject)):
#     for j in range(len(verb)):
#         for k in range(len(object)):
#             print (subject[i],verb[j],object[k])



#########################################################################

#                  Find The Largest Number and Smallest Number


def get_largest(nums):

    largest=nums[2]

    for num in nums:
         if num < largest:
            largest = num
    return largest




for i in range(5):

    num= int(input("ENter a num"))
    larg=get_largest(num)
    print("The Largest Number is:",larg)


################################################################################
           # Remove Duplicate Character From a String  



