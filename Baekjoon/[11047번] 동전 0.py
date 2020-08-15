n,k=map(int,input().split())
a=[0]*n
for i in range(n):
    a[i]=int(input())
cnt=0
a.reverse()
print(a)
for i in range(len(a)):
    if(a[i]<=k):
        while(k>a[i]):
            k=k-a[i]
            print(k)
            cnt+=1
            
    else:
        continue
print(cnt)
