'''
11. Write a Python program to compute and return the square root of a given 'integer'. Go to the editor
Input : 16
Output : 4
Note : The returned value will be an 'integer'
'''
import math


def sqrt_num(n):
    return int(math.sqrt(n))

n=int(input("Enter number: "))
print(sqrt_num(n))