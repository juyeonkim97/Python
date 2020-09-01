#그리디 알고리즘
#백준 1080번

n,m=map(int,input().split())
A=list()
B=list()
cnt=0
for i in range(n):
    A.append(list(map(int,input())))
for i in range(n):
    B.append(list(map(int,input())))
for i in range(n-2):
    for j in range(m-2):
        if A[i][j]!=B[i][j]:
            cnt+=1
            for I in range(i,i+3):
                for J in range(j,j+3):
                    if A[I][J]==0:
                        A[I][J]=1
                    else:
                        A[I][J]=0

if A==B:
    print(cnt)
else:
    print(-1)
