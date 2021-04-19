n=int(input())
a=list()
a=[list(map(int,input().split())) for _ in range(n)] #input 반복문
res=0
s=e=n//2
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if(i<n//2):
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)

