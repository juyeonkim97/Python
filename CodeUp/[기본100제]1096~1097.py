#1096 2차원 배열 초기화하고 값 넣기
n=int(input())
a=[[0]*20 for i in range(20)]
for i in range(n):
    x,y=map(int,input().split())
    a[x][y]=1
for i in range(1,20):
    for j in range(1,20):
        print(a[i][j],end=" ")
    print()
    
#1097 2차원 배열 여러 줄 입력 받기
a=[[0]*20 for i in range(20)]
for i in range(1,20):
    on=list(map(int,input().split()))
    for j in range(19):
        a[i][j+1]=on[j]
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    for j in range(1,20):
        if(a[x][j]==0):
            a[x][j]=1
        else:
            a[x][j]=0
    for j in range(1,20):
        if(a[j][y]==0):
            a[j][y]=1
        else:
            a[j][y]=0
for i in range(1,20):
    for j in range(1,20):
        print(a[i][j],end=" ")
    print()
