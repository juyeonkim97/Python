def check(x):
    if(x==x[::-1]):
        return 1
    return 0

##a=list()
##for _ in range(7):
##    tmp=list(map(int,input().split()))
##    tmp.append(0)
##    a.append(tmp)
               
a=[list(map(int,input().split())) for _ in range(7)]
cnt=0
for i in range(7):
    for j in range(3):
        tmp=a[i][j:j+5]
        cnt+=check(tmp)
tmp=[0]*5
for i in range(7):
    for j in range(3):
        tmp=[a[j+z][i] for z in range(5)]
        cnt+=check(tmp)
print(cnt)
