


# Majority element find krny ha


# num=[2,3,4,5]

# split hamrry pas as a list kam krti ha

num=input("Enter a number: ").split()

num.sort()
count=0
n=len(num)//2 

maj_ele = num[0]

for i in range (len(num)):
    if maj_ele==num[i]:
        count+=1
    else:
        count=1
        maj_ele = num[i]

    if count > n:
        print("Majority element",maj_ele)
        break

    
    # num=num[i]

print(num)
# print(n)