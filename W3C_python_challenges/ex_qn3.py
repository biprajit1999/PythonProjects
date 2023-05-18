def pow_four(n):
    while(n%4==0):
        n/=4
    return n==1
n=int(input("Enter num: "))
print(pow_four(n))