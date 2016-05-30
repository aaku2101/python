#program to check if the function is integer

def is_int(x):
    num=round(x)
    cond=x-num
    if type(x) == int: 
        return True
    elif type(x) == float:
        if cond >0:
            return False
        elif cond==0:
            return True
        else:
            return False
    else:
        return False

var= raw_input("write any number to check : ")
print is_int(var)