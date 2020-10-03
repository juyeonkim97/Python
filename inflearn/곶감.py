n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h,t,k=map(int,input().split())
    for j in range(k):
        if(t==0):#왼쪽으로 미는 경우
            tmp=a[h-1].pop(0)#맨앞에 것 뽑아서
            a[h-1].append(tmp)#맨 뒤로
            
        else:#오른쪽으로 미는 경우
            tmp=a[h-1].pop()#맨뒤에 것 뽑아서
            a[h-1].insert(0,tmp)#맨 앞으로

n2=n//2
res=0
for i in range(n2+1):
    for j in range(i,n-i):
        if(i!=n2):
            res+=a[i][j]
            res+=a[n-1-i][j]
        else:
            res+=a[i][j]
print(res)
