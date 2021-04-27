ef DFS(L,sum):
    global min
    if(sum>m or L>min):
        return
    if(sum==m):
        if(min>L):
            min=L
    else:
        for i in a[::-1]:
            DFS(L+1,sum+i)
            
    
n=int(input())
a=list(map(int,input().split()))
m=int(input())

min=2147000000
DFS(0,0)
print(min)
