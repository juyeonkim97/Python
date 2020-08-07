#1078
a=int(input())
sum=0
for i in range(a+1):
    if(i%2==0):
        sum=sum+i
print(sum)

#1079
a=input().split()
for i in a:
    if i=='q':
        print(i)
        break
    else:
        print(i)

#1080
n=int(input())
sum=0
for i in range(n+1):
    sum+=i
    if sum>= n:
        print(i)
        break

#1081
n,m=map(int,input().split())
for i in range(1,n+1):
    for j in range(1,m+1):
        print("%d %d"%(i,j))
