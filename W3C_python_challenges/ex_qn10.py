'''
10. Write a Python program to find three numbers from an array such that the sum of three numbers equal to a given number.Go to the editor
Input : [1, 0, -1, 0, -2, 2], 0)
Output : [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
'''

def eq_num(l,n):
    m=sorted(l)
    a=[]

    for i in range(len(m)):
        for j in range(i+1,len(m)):
            for k in range(j+1,len(m)):
                for p in range(k+1,len(m)):
                    if(m[i]+m[j]+m[k]+m[p]==n):
                        a.append([m[i],m[j],m[k],m[p]])

    return a

n=int(input("Enter range: "))

l=[]
for i in range(n):
     i=int(input())
     l.append(i)
m=int(input("Enter number: "))

print(eq_num(l,m))
