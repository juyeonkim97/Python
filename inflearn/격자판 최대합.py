n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
res=list()
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    res.append(sum1)
    res.append(sum2)

m=n-1
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][m-i]
res.append(sum1)
res.append(sum2)  
print(max(res))
