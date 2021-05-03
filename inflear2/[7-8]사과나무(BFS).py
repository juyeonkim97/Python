from collections import deque
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,0,1,0] #방향 탐색을 위한 리스트
dy=[0,1,0,-1]
ch=[[0]*n for _ in range(n)]
res=0
x=y=n//2
ch[x][y]=1
res+=a[x][y]
dq=deque()
dq.append((x,y))
L=0
while dq:
    if L==n//2:
        break
    size=len(dq) #L이 0인 경우 한 번, L이 1이면 네 번

    for i in range(size):
        tmp=dq.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if(ch[x][y]==0):
                res+=a[x][y]
                ch[x][y]=1
                dq.append((x,y))
    L+=1

print(res)
