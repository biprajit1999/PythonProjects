'''
1. Write a Python program to check if a given positive integer is a power of two.
Input : 4
Output : True
'''
import math
def pow_two(n):
   return n>0 and (n & (n-1)==0)

n=int(input("Enter number: "))

print(pow_two(n))
