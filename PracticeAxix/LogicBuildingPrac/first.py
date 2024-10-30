


# yeh code chal rha ha


value= str(input("Enter a Character to check: "))

def valid_paranthese(s):
        
        # sb sy phally dehky ik empty list banay gy
        store_values = [] 
        
        # mere jo values ha us jo start bracket ha us k store krway gy

        bracket=['(','[','{']

        # for ka loop iteration k liye jo 

        for cha in s: 

            if cha in bracket: 

                store_values.append(cha) 
                print(cha)

                # mere pas jo input ai ha us k store krwa rha ho ik res  variable k ander
            else:
                 if ( not store_values or  cha =='('and store_values !=')' or cha =='{' and store_values !='}' or cha=='[' and store_values!=']'):
                      return False
                 
                      store_values.pop()
        
        return  "The function is ended"
                      
                 



####################################################################################333333




# def valid_paranthese(s):
        
#         # sb sy phally dehky ik empty list banay gy
#         # store_values = [] 
        
#         # mere jo values ha us jo start bracket ha us k store krway gy

#         bracket=['(','[','{',')',']','}']

#         # for ka loop iteration k liye jo 

#         for cha in s: 

#             if cha in bracket: 
                 
#                  pass

#                 # store_values.append(cha) 

#                 # mere pas jo input ai ha us k store krwa rha ho ik res  variable k ander
#             else:
#                  if ( not bracket or  cha==')'and bracket[-1]!='(' or cha=='}' and bracket !='{' or cha==']' and 
#                     bracket!='['):
#                       return False
                 
#                  bracket.pop()
        
#         return not bracket
                      




















# def valid_paranthese(s):
#         store_values = [] 
#         bracket=['(','[','{']
#         for c in s: 
#             if c in bracket: 
#                 res=store_values.append(c) 
#                 print(res)
#             
#         return not store_values
                         

if valid_paranthese(value):
    print("true")
else:
    print("false")














