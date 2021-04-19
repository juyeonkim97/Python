n=int(input())
a=list()
for i in range(n):
    tmp=list(map(int,input().split())) #n줄 input 반복문
    a.append(tmp)
b=list()
tmp3=0
tmp4=0
for i in range(n):
    tmp=0
    tmp2=0
    tmp3+=a[i][n-1-i]
    tmp4+=a[i][i]
    for j in range(n):
        tmp+=a[i][j]
        tmp2+=a[j][i]
    b.append(tmp)
    b.append(tmp2)
print(max(b))
