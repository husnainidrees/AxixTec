

# # hum ny ik traiagle k elemnt k print krwana ha shortest path jo ha 


# lst=[
    
#     [5],
#     [4,3],
#     [6,7,8],
#     [4,5,6,2]
#     ]




# def mimimum(triangle):
#     n=len(triangle)
#     dp =triangle[-1]
#     all_sum=sum(dp)
#     for i in range(n-2,-1,-1):
#         for j in range(len(lst[i])):

#             if dp[j]< dp[j+1]:
#                 small_value=dp[j]
#             else:
#                 small_value=dp[j+1]

#         dp[j]=((triangle[i][j]) +  (small_value))


#         # all_sum.append(sum(dp[:len(triangle[i])]))
#         # all_sum.append(sum(dp[:len(triangle[i])]))

#         # min_sum = min(all_sum)
    
#     return all_sum

         




# res=mimimum(lst)

# print(res)











triangle = [
     [5],
    [4, 3],
   [6, 7, 8],
  [4, 5, 6, 2]
]



def minimumTotal(triangle):
   
    n = len(triangle)

    dp = triangle[-1]
    
   
    all_sums = [sum(dp)]  
    
    for i in range(n-2, -1, -1):
        for j in range(len(triangle[i])):
          
            if dp[j] < dp[j+1]:
                smaller_value = dp[j]
            else:
                smaller_value = dp[j+1]
            
            dp[j] = triangle[i][j] + smaller_value
        
        all_sums.append(sum(dp[:len(triangle[i])]))

    min_sum = min(all_sums)
    
    return  all_sums 


min_sum, all_sums = minimumTotal(triangle)



print("all  after each step", all_sums)
print("minimum sum", min_sum)








