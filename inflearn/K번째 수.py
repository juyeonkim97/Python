t=int(input())
b=list()
klist=list()
for i in range(t):
    n,s,e,k=map(int,input().split())
    a=list(map(int,input().split()))
    a=sorted(a[s-1:e])
    klist.append(k)
    b.append(a)
print(klist)
for i in range(t):
    print("#{} {}".format(i+1,b[i][klist[i]-1]))
