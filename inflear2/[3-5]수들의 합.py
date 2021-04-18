n,m=map(int,input().split())
a=list(map(int,input().split()))
lt=0
rt=1
tot=a[lt]
cnt=0
while (True): #sum 슬라이스 말고 범위 안에 값들 합하는 법
    if(tot<m):
        if(rt<n):
            tot+=a[rt]
            rt+=1
        else:
            break
    elif(tot==m):
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1

print(cnt)
        
