n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    idx,lr,mv=map(int,input().split())
    for _ in range(mv):
        if(lr==0):
            tmp=a[idx-1].pop(0) #리스트 추가 삭제
            a[idx-1].append(tmp)
        else:
            tmp=a[idx-1].pop(n-1)
            a[idx-1].insert(0,tmp)
s=0
e=n
res=0
for i in range(n):
    for j in range(s,e):
        res+=a[i][j]
    if(i<n//2):
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
        
    
        
