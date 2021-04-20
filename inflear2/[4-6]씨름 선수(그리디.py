n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
a.sort()
cnt=0
ch=[1]*n
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i][1]<a[j][1]):
            ch[i]=0
            break
print(sum(ch))
        
