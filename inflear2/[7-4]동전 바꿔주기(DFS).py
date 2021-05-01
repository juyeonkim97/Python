def DFS(L,sum):
    
    global cnt
    if(sum>t):
        return
    if(L==k):
        if(sum==t):
            cnt+=1
    else:
        for j in range(b[L]+1):
            DFS(L+1,sum+a[L]*j)
t=int(input())
k=int(input())
a=list()
b=list()
for i in range(k):
    c,d=map(int,input().split())
    a.append(c)
    b.append(d)
cnt=0
DFS(0,0)
print(cnt)
