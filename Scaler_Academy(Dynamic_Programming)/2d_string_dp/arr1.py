n = list(map(int,input().split()))
print(n)
l=[]
for i in range(len(n)):
    sm = 0
    lg = 0
    for j in range(i+1, len(n)):
        if(n[j]<n[i]):
            sm += n[j]
        else:
            lg += n[j]
    k = sm*lg
    l.append(k)

print(l)