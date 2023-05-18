'''
7. Write a Python program to find a missing number from a list. Go to the editor
Input : [1,2,3,4,6,7,8]
Output : 5
'''

def find_miss(l):
    m=sorted(l)
    for i in range(m[0],m[-1]):
        if i not in m:
            print(i)
        else:
            continue

n=int(input("Enter range of list: "))
l=[]
for i in range(n):
    i=int(input())
    l.append(i)
find_miss(l)