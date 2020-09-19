n,m=map(int,input().split())
sumlist=[0]*(n+m+1)
for i in range(1,n+1):
    for j in range(1,m+1):
        sumlist[i+j]+=1
maxnum=max(sumlist)
for i in range(len(sumlist)):
    if(sumlist[i]==maxnum):
        print(i,end=" ")
        

