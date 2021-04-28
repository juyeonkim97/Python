def DFS(L):
    global cnt
    if(L==m):
        for j in res:
            print(j,end=" ")
        print()
        cnt+=1
        return
    else:
        for i in range(1,n+1):
            
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)#dfs 밑이 호출 후 되돌아 온 후에 지나가는 거
                ch[i]=0 #호출 후 되돌아 온 후 ch 풀어줘야 함....
                
        


n,m=map(int,input().split())
ch=[0]*(n+1)
res=[0]*m
cnt=0
DFS(0)
print(cnt)
