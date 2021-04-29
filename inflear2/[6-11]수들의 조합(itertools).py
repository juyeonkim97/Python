from itertools import combinations as cb
n, k=map(int, input().split())
a=list(map(int, input().split()))
m=int(input())
cnt=0
for i in cb(a,k):
    tmp=sum(i)
    if(tmp%m==0):
        cnt+=1
print(cnt)
