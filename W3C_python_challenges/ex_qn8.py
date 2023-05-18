'''
8. Write a Python program to find missing numbers from a list. Go to the editor
Input : [1,2,3,4,6,7,10]
Output : [5, 8, 9]
'''

def missing_list(l):
    m=sorted(l)

    n=[]
    for i in range(m[0],m[-1]):
        if i not in m:
            n.append(i)

    return (n)

n=int(input("Enter range of the list: "))
l=[]
for i in range(n):
    i=int(input())
    l.append(i)

print(missing_list(l))