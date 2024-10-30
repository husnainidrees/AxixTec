
# valid paranthers


def is_valid(s):

    brack_map={
    ")":"(",
    "}":"{",
    "]":"[",
    }

    stack=[]

    for char in s:
        if char in brack_map:
            top_elem = stack.pop() if stack else "#"
            if brack_map[char]!=top_elem:
                return False
        else:
             stack.append(char)
    return not stack




s="()"

print(is_valid(s))




def is_Valid(s):

    map={

        ')':'(',
        '}':'{',
        ']':'[',

    }

    stack=[]

    for char in s:
        if char in map:
            top_el=stack.pop() if stack else "#"
            if map[char]!= top_el:
                return False
            else:
                stack.append(char)
    
    return not stack
                

        


