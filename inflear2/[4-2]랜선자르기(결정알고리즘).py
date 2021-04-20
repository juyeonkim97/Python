def count(mid):
    cnt=0
    for x in a:
        cnt+=x//mid
    return cnt

k,n=map(int,input().split())
a=list()
for _ in range(k):
    tmp=int(input())
    a.append(tmp)
lt=0
rt=max(a)
while lt<=rt:
    cnt=0
    mid=(lt+rt)//2
    if(cnt>=n): #커진 상황에서도 계속 진행해야 최적의 값이 나옴...
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)
