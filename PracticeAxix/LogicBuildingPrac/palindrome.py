
st=str(input("Enter the string"))

def is_palin(s):

    rev=s[::-1]

    if rev==st:

        return True
    else:
        return False
    



is_palin(st)

