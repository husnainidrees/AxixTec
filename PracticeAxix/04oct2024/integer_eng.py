

# Number to Word

def num_to_word(num):
    if num ==0:
        return "zero"
    below_20 =['','one','two','three','four','five','six','seven','eight','nine','ten',]


    tens=['','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']

    thousand =['','thousand']

    def func(n):
        if n < 20:
            return below_20[n]
        elif n < 100:
            return tens[n//10] + ('' if n%10 == 0 else '' + below_20 [n%10])
        elif n < 1000:
            return below_20[n//100] + 'hundered' + ('' if n%100==0 else ' ' + func(n%100))
        else:
            for i ,word in enumerate(thousand):
                if n<1000 **(i+1):
                    return func(n//(1000** i)) + thousand[i] + ('' if n%(1000**i)==0 else ' ' + func (n%1000**i))


    
    
    return func(num).strip()
    





print(num_to_word(123))




