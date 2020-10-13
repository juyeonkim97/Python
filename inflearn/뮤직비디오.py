def Count(capacity):
    cnt=1
    tmp=0
    for i in a:
        if(tmp+i<=capacity):
            tmp+=i
        else:
            cnt+=1
            tmp=i
    return cnt
n,m=map(int,input().split())
a=list(map(int,input().split()))
lt=1
rt=sum(a)
cnt=1
tmp=0
while(lt<=rt):
    mid=(lt+rt)//2
    if(Count(mid)<=m):#2장으로 나눠진다는 것은 3장으로도 나눠진다는 거래...
        #6으로 나눠지는 건 2로도 나눠진다 이건가
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)

        
