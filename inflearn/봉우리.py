n=int(input())
a=[list(map(int,input().split())) for _ range(n)]
cnt=0
for i in range(n):
    for j in range(n):
        if(i in [0,n-1] and j in [0,n-1]
