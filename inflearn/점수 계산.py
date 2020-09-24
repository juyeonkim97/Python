n=int(input())
a=list(map(int,input().split()))
cnt=1
res=0
for i in a:
    if(i==1):
        res+=cnt
        cnt+=1
    else:
        cnt=1
print(res)
