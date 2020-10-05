n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
a.insert(0,[0]*n)
a.append([0]*n)
for x in a:
    x.insert(0,0)
    x.append(0)
dx=[-1,1,0,0]#상하좌우 움직이는 변수
dy=[0,0,-1,1]
cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
