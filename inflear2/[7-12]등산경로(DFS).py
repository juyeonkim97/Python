def DFS(x,y):
    global cnt
    global board
    global ch
    if x==ex and y==ey:
        cnt+=1
        return
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1 #한 번 갔던 곳은 체크
                DFS(xx,yy)
                ch[xx][yy]=0 #다시 되돌아 오면 체크 풀기
            
n=int(input())
min=2147000000
max=-2147000000
board=list()
for i in range(n): #최솟값, 최댓값 위치 찾기
    tmp=list(map(int,input().split()))
    board.append(tmp)
    for j in range(n):
        if tmp[j]<min:
            min=tmp[j]
            sx=i
            sy=j
    for j in range(n):
        if tmp[j]>max:
            max=tmp[j]
            ex=i
            ey=j

ch=[[0]*n for _ in range(n)]
dx=[-1,0,1,0] #방향 탐색을 위한 리스트
dy=[0,1,0,-1]
x=sx
y=sy
cnt=0
ch[x][y]=1
DFS(sx,sy)
print(cnt)
