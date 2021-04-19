n=int(input())
a=list()
for _ in range(n):
    tmp=list(map(int,input().split()))
    tmp.insert(0,0)
    tmp.append(0)
    a.append(tmp)
tmp=[0]*(n+1)
a.append(tmp)
a.insert(0,tmp)
cnt=0
#상하좌우 탐색, 네방향 탐색
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(1,n+1):
    for j in range(1,n+1):
        #모두 참이면 트루
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
            
        
