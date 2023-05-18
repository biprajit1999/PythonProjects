n = int(input())

ls = list(map(int,input().split()))
print(ls)
mx = ls[n-1]
cnt = 1
for i in range(n-2,-1,-1):
    if(ls[i]>mx):
       cnt += 1
       mx = ls[i]

print(cnt)