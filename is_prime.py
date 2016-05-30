#program to find whether given positive integer is prime or not
def is_prime(x):
    if x<0:
        return False
    else:
        if x==0 or x==1:
            return False
        elif x==2:
            return True
        else:        
            for var in range(2,x):
                if x%var ==0:
                    return False
            else:
                return True

print is_prime(10)