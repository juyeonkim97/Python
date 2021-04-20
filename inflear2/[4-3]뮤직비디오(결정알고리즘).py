def count(x):
    sum=0
    cnt=0
    for i in a:
        if(sum+i>=x):
            cnt+=1
            sum=i
        else:
            sum+=i
    return cnt
            
    
n,m=map(int,input().split())
a=list(map(int,input().split()))
lt=0
rt=sum(a)
maxx=max(a) #가장 긴 비디오도 담겨야 되니까
while lt<=rt:
    mid=(lt+rt)//2
    cnt=count(mid)
    if(mid>=maxx and cnt>=m):
        lt=mid+1
        res=mid
    else:
        rt=mid-1
print(res)
        
