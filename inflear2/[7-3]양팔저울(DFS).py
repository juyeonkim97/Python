def DFS(L,sum):
    global res #전역변수화 필요함
    if(L==k):
        if(0<sum<=s): #모두 사용하지 않아서 0 되는 것도 뺄 수 있고,
            #음수의 값은 대칭으로 또 나오게 돼있음
            res.add(sum)
            
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum-a[L])
        DFS(L+1,sum)
k=int(input())
a=list(map(int,input().split()))
s=sum(a)
res=set()
DFS(0,0)
print(s-len(res))
