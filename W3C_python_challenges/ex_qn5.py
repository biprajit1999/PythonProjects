'''
5. Write a Python program to check if an integer is the power of another integer.Go to the editor
Input : 16, 2
Output : True
'''
def is_power(x, y):
   while (x%y == 0):
       x = x / y
   return x == 1

m=int(input("Enter power no: "))
n=int(input("Enter number: "))

print(is_power(m,n))