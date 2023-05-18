# 2. Write a Python program to check if a given positive integer is a power of three.

def pow_three(n):
    while(n%3==0):
        n/=3
    return n==1

n=int(input("Enter num:  "))

print(pow_three(n))