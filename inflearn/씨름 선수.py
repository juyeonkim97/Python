n=int(input())
a=list()
for i in range(n):
    l,w=map(int,input().split())
    a.append((l,w))
a.sort(reverse=True)
wmax=a[0][1]
cnt=1
for i in range(1,n):
    if(wmax<a[i][1]):
        cnt+=1
        wmax=a[i][1]
print(cnt)
