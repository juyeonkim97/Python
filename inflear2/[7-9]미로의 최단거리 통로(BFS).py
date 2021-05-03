from collections import deque
a=[list(map(int,input().split())) for _ in range(7)]
dx=[-1,0,1,0] #방향 탐색을 위한 리스트
dy=[0,1,0,-1]
dis=[[0]*7 for _ in range(7)]
x=y=0 #출발은 1,1 -> 0,0
a[x][y]=1
dq=deque()
dq.append((x,y))
a[x][y]=1 #한 번 방문한 곳 벽으로 만들어버리기
while dq:
    tmp=dq.popleft()
    for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if 0<=x<=6 and 0<=y<=6 and a[x][y]==0:
                a[x][y]=1
                dis[x][y]=dis[tmp[0]][tmp[1]]+1
                dq.append((x,y))

if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])
