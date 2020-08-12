#1098
h,w=map(int,input().split())
n=int(input())
a=[[0]*w for i in range(h)]
for i in range(n):
    l,d,x,y=map(int,input().split())
    if (d==0):
        for j in range(l):
            a[x-1][y-1]=1
            y+=1
            j+=1
    else:
        for j in range(l):
            a[x-1][y-1]=1
            x+=1
            j+=1
for i in range(h):
    for j in range(w):
        print(a[i][j],end=" ")
    print()

#1099
a=[[0]*11 for i in range(11)]
for i in range(1,11):
    n=list(map(int,input().split()))
    for j in range(1,11):
        a[i][j]=n[j-1]
x,y=2,2
while (True):
    if a[x][y]==0 :
        a[x][y]=9
    elif a[x][y]==2 :
        a[x][y]=9
        break
    if (a[x][y+1]==1 and a[x+1][y]==1) or (x==9 and y==9) :
        break
    if a[x][y+1]!=1 :
        y+=1
    elif a[x+1][y]!=1 :
        x+=1
for i in range(1,11):
    for j in range(1,11):
        print(a[i][j],end=" ")
    print()
