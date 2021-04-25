##def DFS(L):
##    global cnt
##    if(res==0):
##        return
##    else:
##        for i in a:
##            cnt+=res//i
    
n=int(input())
a=list(map(int,input().split()))
m=int(input())

a.sort(reverse=True)
res=m
cnt=0
for i in a:
    cnt+=res//i
    res=res%i
    if(res==0):
        break


print(cnt)
        
        
    
    
