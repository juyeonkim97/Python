n,k=map(int,input().split())
num=list(map(int,input().split()))
res=set()
for i in range(len(num)):
    for j in range(i+1,len(num)):
        for z in range(j+1,len(num)):
            res.add(num[i]+num[j]+num[z])
res=list(res)
res.sort(reverse=True)
print(res[2])
