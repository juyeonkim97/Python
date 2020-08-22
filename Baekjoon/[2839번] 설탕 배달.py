#그리디 알고리즘
#백준 2839번

n=int(input())
cnt=0
for i in range(1667):
    for j in range(1001):
        if(3*i+5*j==n):
            cnt=i+j
            break
    if(cnt!=0):
        break
if(cnt==0):
    print(-1)
else:
    print(cnt)
