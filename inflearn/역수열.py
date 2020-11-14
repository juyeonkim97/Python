n=int(input())
a=list(map(int,input().split()))
b=[0]*n
for i in range(n):
    for j in range(n):
        if(a[i]== 0 and b[j]==0):
            b[j]=i+1
            break
        elif(b[j]==0):
            a[i]-=1     

for i in b:
    print(i,end=" ")
