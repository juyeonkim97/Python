def DFS(L,sum,tsum):
    global result
    if(sum+(total-tsum)<result):#이것보다 더 좋은 값은 안 나옴
        return
    if(sum>c):
        return
    if(L==n):
        if(result<sum):
            result=sum #global 안 쓰면 이 구문으로 인해 로컬변수화 됨
    else:
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])
        
c,n=map(int,input().split())
a=[int(input()) for _ in range(n)]
result=-2147000000
total=sum(a)
DFS(0,0,0)
print(result)

