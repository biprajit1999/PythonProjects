def c_chng(ar,n,m):

    table = [0 for i in range(m+1)]
    table[0] = 1

    for i in range(n):
        for j in range(ar[i],m+1):
            table[j]+=table[j-ar[i]]

    return table[m]


ar=[1,2,3]
n=len(ar)
m=4

print(c_chng(ar,n,m))