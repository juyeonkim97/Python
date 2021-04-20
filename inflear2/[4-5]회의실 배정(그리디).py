n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
a.sort(key=lambda x :(x[1],x[0]))
cnt=1
now=a[0]
for i in range(len(a)):
    if(now[1]<=a[i][0]):
        cnt+=1
        now=a[i]
print(cnt)
