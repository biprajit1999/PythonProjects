'''
9. Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero. Go to the editor
Input : [-1,0,1,2,-1,-4]
Output : [[-1, -1, 2], [-1, 0, 1]]
Input : [-25,-10,-7,-3,2,4,8,10]
Otput : [[-10, 2, 8], [-7, -3, 10]]
Note : Find the unique triplets in the array.
'''

def unique_trip(l):
    m=sorted(l)
    a=[]
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            for k in range(j+1,len(m)):
                if(m[i]+m[j]+m[k]==0):
                    a.append([m[i],m[j],m[k]])

    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(a[i]==a[j]):
                a.remove(a[i])
    return a

n=int(input("Enter range: "))

l=[]
for i in range(n):
    i=int(input())
    l.append(i)

print(unique_trip(l))