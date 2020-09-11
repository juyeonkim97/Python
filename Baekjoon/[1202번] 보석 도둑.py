#그리디 알고리즘
#백준 1202번

import sys
n,k=map(int,sys.stdin.readline().split())#보석갯수, 가방 갯수
a=list()
for i in range(n):
    m,v=map(int,sys.stdin.readline().split())
    a.append((m,v))#무게, 가격
##a=sorted(a, key=lambda a:a[0],reverse=True)
a.sort()
c=list()#최대 무게
for i in range(k):
    info=int(input())
    c.append(info)
c.sort()
res=0
j=0
for j in c:
    maxnum=0
    for i in range(len(a)):
        if(a[i][0]<=j):
            if(maxnum<=a[i][1]):
                maxnum=a[i][1]
        else:
            res+=maxnum
print(res)

