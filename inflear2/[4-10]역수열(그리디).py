n=int(input())
a=list(map(int,input().split()))
res=[0]*n
for i in range(n):
    j=0
    cnt=0
    while cnt!=a[i]:
        if(res[j]==0):
            cnt+=1
            j+=1
        else:
            j+=1
    while True:
        if(res[j]!=0):
            j+=1
        else:
            res[j]=i+1
            break
for i in res:
    print(i,end=" ")
    
    
    
