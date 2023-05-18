# Here is the source code of a Python program to print the nth Fibonacci number using dynamic programming with bottom-up approach. The program output is shown below.
#Buttom up approach

def fib(n):
    if(n==0):
        return 0

    r=[-1]*(n+1)
    r[0]=0
    r[1]=1

    for i in range(2,n+1):
        r[i]=r[i-1]+r[i-2]

    return r[n]

n=7
print(fib(n))