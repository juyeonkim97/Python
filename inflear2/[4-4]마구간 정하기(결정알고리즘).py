def count(x):
    cnt=1
    ep=a[0] #ep는 마지막 배치한 말의 좌표, 첫 자리에 말 배치하고 시작
    for i in range(1,n):
        if (a[i]-ep >= x): #크거나 같으면 배치
            ep=a[i]
            cnt+=1
    return cnt

n,c=map(int,input().split())
a=[int(input()) for _ in range(n)]
a.sort()
lt=a[0]
rt=a[-1]
while lt<=rt:
    mid=(lt+rt)//2
    cnt=count(mid)
    if(cnt>=c):
        lt=mid+1
        res=mid
    else:
        rt=mid-1

print(res)
