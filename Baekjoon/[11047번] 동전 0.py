#그리디 알고리즘
#백준 11047번

n,k=map(int,input().split())
a=[0]*n
for i in range(n):
    a[i]=int(input())
cnt=0
a.reverse()
for i in range(len(a)):
    if(a[i]<=k):
        tmp=int(k/a[i])
        k=k%a[i]
        cnt+=tmp
    else:
        continue
print(cnt)
