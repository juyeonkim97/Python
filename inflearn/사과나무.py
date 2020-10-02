n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
res=0
m=n//2
for i in range(m+1):
    for j in range(m-i,m+1+i):
        if(i!=m):
            res+=a[i][j]
            res+=a[n-1-i][j]
        else:
            res+=a[i][j]
print(res)

