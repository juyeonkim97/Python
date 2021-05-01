def DFS(L):
    global res
    global money
    if(L==n):
        tmp=max(money)-min(money)
        if tmp<res:
            tmp2=set()#세개가 모두 다른지 확인 
            for x in money:
                tmp2.add(x)
            if len(tmp2)==3:
                res=tmp
            
    else:
        for i in range(3):
            money[i]+=a[L]
            DFS(L+1)
            money[i]-=a[L]

n=int(input())
a=[int(input()) for _ in range(n)]
money=[0]*3
res=2147000000
DFS(0)
print(res)
