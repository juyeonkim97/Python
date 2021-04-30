def DFS(L,tsum,ssum):
    global max
    if(tsum>m):
        return
    if L==n:
        if(ssum>max):
            max=ssum
    else:
        DFS(L+1,tsum+time[L],ssum+score[L])
        DFS(L+1,tsum,ssum)
            
            
            
n,m=map(int,input().split())
time=list()
score=list()
for i in range(n):
    a,b=map(int,input().split())
    score.append(a)
    time.append(b)
max=-2147000000
DFS(0,0,0)
print(max)

