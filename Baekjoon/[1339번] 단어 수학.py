#그리디 알고리즘
#백준 1339번

import sys
n=int(sys.stdin.readline())
strlist=list()
sum=0
num=9
for i in range(n):
    a=list(input())
    a.reverse()    
    strlist.append(a)
strlist.sort(key=len,reverse=True)
pointlist=[0]*26
for i in range(n):
    mult=1
    for j in range(len(strlist[i])):
        pointlist[ord(strlist[i][j])-65]+=mult*1
        mult*=10
pointlist.sort(reverse=True)
for i in pointlist:
    sum+=i*num
    num-=1
    if i==0:
        break
print(sum)
