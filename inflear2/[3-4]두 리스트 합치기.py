n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=a+b
c.sort()
for i in range(len(c)):
    print(c[i],end=" ")


#sort 함수 안 쓰고 구현하기
##n=int(input())
##a=list(map(int, input().split()))
##m=int(input())
##b=list(map(int, input().split()))
##p1=p2=0
##c=[]
##while p1<n and p2<m:
##    if a[p1]<b[p2]:
##        c.append(a[p1])
##        p1+=1
##    else:
##        c.append(b[p2])
##        p2+=1
##if p1<n:
##    c=c+a[p1:]
##if p2<m:
##    c=c+b[p2:]
##for x in c:
##    print(x, end=' ')
