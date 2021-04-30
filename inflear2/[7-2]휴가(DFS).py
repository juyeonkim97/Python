def DFS(L,psum):
    global max
    if L==n+1:
        if(psum>max):
            max=psum
    else:
        if L+time[L]<=n+1:
            DFS(L+time[L],psum+point[L])
        DFS(L+1,psum)
            
            
            
n=int(input())
time=[0]
point=[0]
for i in range(n):
    a,b=map(int,input().split())
    time.append(a)
    point.append(b)

max=-2147000000
DFS(1,0)
print(max)

