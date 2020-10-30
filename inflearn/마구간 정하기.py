#가장 가까운 두 말의 최대 거리라는 말은 가장 가까운 두 말의 거리가 3이라면
#모든 말들의 거리가 3보다 크거나 같아야 된다는 말.
def Count(len):
    cnt=1
    ep=a[0]#end point 끝에 있는 말.
    for i in range(1,n):
        if(a[i]-ep>=len):
            cnt+=1
            ep=a[i]
    return cnt
n,c=map(int,input().split())
a=[int(input()) for _ in range(n)]
a.sort()
#마구간 좌표 범위
lt=a[0]
rt=a[n-1]
while(lt<=rt):
    mid=(lt+rt)//2 #이 값이 가장 가까운 두 말의 거리임. 위치 아니고.
    if(Count(mid)>=c):
        res=mid
        lt=mid+1 #만약에 2에서 부합하더라도 rt 전까지는 계속 검사해봐야 최적의 답이 나
    else:
        rt=mid-1
print(res)
