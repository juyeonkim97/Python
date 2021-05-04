def DFS(x,y):
    global cnt
    global board
    if x==6 and y==6:
        cnt+=1
        return
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
                board[xx][yy]=1 #한 번 갔던 곳은 체크
                DFS(xx,yy)
                board[xx][yy]=0 #다시 되돌아 오면 체크 풀기
            
board=[list(map(int,input().split())) for _ in range(7)]
dx=[-1,0,1,0] #방향 탐색을 위한 리스트
dy=[0,1,0,-1]
x=y=0 #출발은 1,1 -> 0,0
cnt=0
board[x][y]=1
DFS(0,0)
print(cnt)
