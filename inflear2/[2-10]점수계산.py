n=int(input())
a=list(map(int,input().split()))
res=0
for i in range(len(a)):
    s=slice(0,i+1)#슬라이싱에 변수 넣는 법
    if(a[i]==1):
        if(sum(a[s])>=1):#sum을 cnt변수로 대체하면 됨,,,,,,,,
            res+=sum(a[s])
    else:
        a[s]=[0]*(i+1)
print(res)
