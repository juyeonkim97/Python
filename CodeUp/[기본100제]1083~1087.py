#1083
n=int(input())
for i in range(1,n+1):
    if(i%3==0):
        print("X",end=" ")
    else:
        print(i,end=" ")

#1084
r,g,b=map(int,input().split())
cnt=0
for i in range(r):
    for j in range(g):
        for z in range(b):
            print("%d %d %d"%(i,j,z))
            cnt+=1
print(cnt)

#1085
h,b,c,s=map(int,input().split())
result=h*b*c*s
print("%.1f MB"%(result/8/1024/1024))

#1086
w,h,b=map(int,input().split())
result=w*h*b
print("%.2f MB"%(result/8/1024/1024))

#1087
n=int(input())
sum=0
for i in range(n+1):
    sum+=i
    if(sum>=n):
        print(sum)
        break
