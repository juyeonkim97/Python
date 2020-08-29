#그리디 알고리즘
#백준 1339번

import sys
n=int(sys.stdin.readline())
strlist=list()
sum=0
num=9
for i in range(n):
    a=list(input())
    strlist.append(a)
pointlist=[0]*26
for i in range(n):#자리별로 가중치 계산
    tmp=len(strlist[i])
    for j in range(tmp):
        pointlist[ord(strlist[i][j])-65]+=1*(tmp-j)
for i in range(n):
    strlist[i][0]=pointlist[ord(strlist[i][0])-65]
strlist=sorted(strlist,key=lambda strlist:strlist[0])
strlist.sort(key=len,reverse=True)
print(strlist)
##for i in range(n):
##    for j in range(len(strlist[i])):
##        pointlist[ord(strlist[i][j])-65]+=1*(tmp-j)
##for i in range(n):
##    mult=1
##    for j in range(len(strlist[i])):
##        tmp=abclist.index(strlist[i][j])#abclist에서 찾고
##        sum=sum+afabclist[tmp]*mult#afabclist 값 대입
##        mult*=10
##print(sum)
