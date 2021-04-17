n,m=map(int,input().split())
a=[0]*(n+m+1) #0으로 초기화하면서 리스트 생성
for i in range(1,n+1):
    for j in range(1,m+1):
        a[i+j]+=1
maxnum=max(a)
for i in range(len(a)):
    if(maxnum==a[i]):
        print(i,end=" ")
