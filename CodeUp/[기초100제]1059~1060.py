#1059 비트단위논리연산
a= int(input())
print("%d"%(-a-1))

#1060
a,b=map(int,input().split())
c=int(bin(a&b),2)
print(c)
