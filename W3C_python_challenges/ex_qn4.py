import math


def perfect_sq(n):
    if(math.ceil(math.sqrt(n))==math.floor(math.sqrt(n))):
        return True
    else:
        return False

n=int(input("Enter Num: "))
print(perfect_sq(n))