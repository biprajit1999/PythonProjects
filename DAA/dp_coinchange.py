def coin_change(arr,m,n):
    table=[0 for i in range(n+1)]
    table[0]=1

    for i in range(m):
        for j in range(arr[i],n+1):
            table[j]+=table[j-arr[i]]

    return table[n]







ar=[1,2,3]
m=len(ar)
n=4
print(coin_change(ar,m,n))