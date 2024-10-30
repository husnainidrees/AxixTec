# def minimumTotal(triangle):
#     # Bottom se start karke top tak calculation karna hai
#     n = len(triangle)
    
#     # Last row ko copy kar lete hain
#     dp = triangle[-1]
    
#     # Sums ko store karne ke liye ek list
#     all_sums = [sum(dp)]  # Initial sum from the last row
    
#     # Bottom-up approach, second last row se le kar top tak
#     for i in range(n-2, -1, -1):
#         for j in range(len(triangle[i])):
#             # Har element ke neeche ke do elements me se chhota element add karo
#             if dp[j] < dp[j+1]:
#                 smaller_value = dp[j]
#             else:
#                 smaller_value = dp[j+1]
            
#             # Neeche ke chhote element ko current element mein add karna
#             dp[j] = triangle[i][j] + smaller_value
        
#         # Har row ka sum calculate karke list mein store karna
#         all_sums.append(sum(dp[:len(triangle[i])]))

#     # Sari sums ka minimum dhoondna
#     min_sum = min(all_sums)
    
#     return min_sum, all_sums  # Minimum sum ke sath sari sums return karenge

# # Example triangle
# triangle = [
#      [2],
#     [3, 4],
#    [6, 5, 7],
#   [4, 1, 8, 3]
# ]

# # Shortest path sum
# min_sum, all_sums = minimumTotal(triangle)

# print("All Sums after each step:", all_sums)
# print("Minimum Sum:", min_sum)














# Yeh Letter A print KR K DY GY 

# result_str=" "
# for row in range(0,7):
#     for column in range(0,7):
#         if(((column==1 or column==5) and row !=0) or ((row == 0 or row ==3) and (column > 1 and column < 5))):
#             result_str=result_str + "*"
#         else:
#             result_str=result_str + " "
        

#     result_str=result_str + "\n"



# print(result_str)
           




# yeh pattern ka code tha ik 

# n=5

# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
    
#     print("")


# # ab hum ny down print krwana ha 

# for i in  range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
    
#     print("")



# def min_total(triangle):
#     for row in range(len(triangle) -2,-1,-1 ):
#         for col in range(len(triangle[row])):
#             # print(triangle[row][col])
#             triangle[row][col] = min(triangle[row+1][col],triangle[row+1][col+1])
    
#     return triangle[0][0]





# def min_total(triangle):
#     for row in range(len(triangle) -2,-1,-1):
#         for col in range(len(triangle[row])):
#             triangle[row][col] + min(triangle[row+1][col],triangle[row+1][col+1])
#         return triangle[0][0]
    


# triangle = [
#      [10],
#     [3, 4],
#    [6, 5, 7],
#   [4, 1, 8, 3]
# ]


# res=min_total(triangle)
# print(res)






# swap the position

# lst1=[1,4,5,6]

# pos1,pos3=1,4

# def swap(lst1,pos1,pos3):
#     temp=lst1[pos1]
#     lst1[pos1]=lst1[pos3]
#     lst1[pos3]=temp

#     return lst1

 

# print(swap(lst1,pos1,pos3-1))








####################################### LEET CODE PROBLEM

# FInd the Longest Substring

# def substring(s):
#     mapSet={}
#     start,result=0,0

#     for end in range(len(s)):
#         if s[end] in mapSet:
#             start=max(mapSet[s[end]],start)

#         result=max(result,end-start+1)
#         mapSet[s[end]]=end+1

#     return result


# st="abcababaaa"

# res=substring(st)
# print(res)




########################## Target and Two Sum Code ##################33


# def Sum(num,target):
#     for i in range(len(num)):
#         for j in range(i+1,len(num)):
#             if (num[i]+num[j]==target):
#                 return i,j
    



# ls=[2,4,5]
# target=6

# res=Sum(ls,target)
# print(res)




# Leet Code Reverse the String


# def reverse(x:int):
#     s=str(x)
#     if s[0]=='-':
#         m=-1
#         s=s[1:]
#     else:
#         m=1
#         a=m*(int(s[::-1]))
#         if a in range(-2**31 or 2**31):
#             return a
#         else:
#             return 0





# ls=[2,3,4]

# re=reverse(ls)
# print(re)


########### For print the first middle and last character

# str1="James"

# res=str1[0]

# # x=len(str1/2)

# mi=int(len(str1)/2)

# print(mi)

# print(res)
# print(str1)


# res=res + str1[mi]

# res=res + str1[len(str1)-1]

# print(res)

    



# def get_middle(str1):

#     mi=int(len(str1)/2)

#     # slicing use ho g
#     res=str1[mi -1:mi + 2]

#     print (res)








# str1="Husnain"
# re = get_middle(str1)
# print(re)




################################# yeh ik sequence hota ha jis mein ap separate krta ho lower or upper ko ######


# str2="HmnUSMa"

# lower=[]
# Upper=[]

# for char in str2:
#     if char.islower():
#         lower.append(char)
#     else:
#         Upper.append(char)



# sorted_str=' '.join(lower + Upper)

# print(sorted_str)




####################################### 
############# FInd Tootal and Count  digit k nikal kr us  k average lena ha #########################



# input_str="as3423@ga222"
# total=0
# cont=0

# for char in input_str:
#     if char.isdigit():
#         total +=int(char)
#         cont+=1



# avg=total/cont


# print("average and total ",total,cont)




############## Product is Divisible by sum or not

# def is_divisible(numbers):
#     if not numbers:
#         return False
    
#     product=1
#     summation=0
#     for num in numbers:
#         product*=num
#         summation+=num
    
#     if summation==0:
#         return False
    

#     return product % summation == 0





# lst=[2,2,2,2]

# res=is_divisible(lst)

# print(res)





############################# COdin question for string related #################################


# def count_st(str1):

#     m=len(str1)

#     for i in range(m):
        
#         return m
    




# str1="waseemali"
# re1=count_st(str1)
# print(re1)





######################## Frequency count Nikalna ha Hum ny ################


def count_fre(str3):

    dict={}

    for n in str3:
        key=dict.keys()
        if n in key:
            dict[n]+=1
        else:
            dict[n]=1

    return dict





print(count_fre("google"))






########################## Replace the specific charcater expect itself 


def chara_ch(str0):

    char=str0[0]

    str0 = str0.replace(char,"&")

    print(str0)

    str0=char + str0[1:] 

    print(str0)

    return str0



print(chara_ch("restart"))


#################### Next problem solving #################






