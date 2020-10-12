def count(len):
    cnt=0
    for x in a:
        cnt+=(x//len)
    return cnt
        
k,n=map(int,input().split())
a=[int(input()) for _ in range(k)]
a.sort(reverse=True)
lt=0
rt=a[0]
while(lt<=rt):
    mid=(lt+rt)//2
    if count(mid)>=n:#n보다 크거나 같다는 건 나누는 길이를 더 늘려야 된다는 것
        #같아도 이 조건을 시행하는 이유는 최대로 긴 것을 찾기 위해
        res=mid
        lt=mid+1
    else:# 나누는 길이를 더 줄여야 됨
        rt=mid-1
print(res)
        
    
        
        
        

