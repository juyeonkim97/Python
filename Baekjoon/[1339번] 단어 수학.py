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
strlist.sort(key=len,reverse=True)#긴 순서대로 정렬
print(strlist)
abclist=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")#abc의 인덱스용
afabclist=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")#숫자로 바꾼 후(after abclist)
abcpointlist=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")#자릿수대로 가중치별로 계산한 리스
for j in range(len(strlist[0]),-1,-1):
    for i in range(n):
        try:
            if strlist[i][j] in afabclist:
                tmp=abclist.index(strlist[i][j])
                afabclist[tmp]=num
                num-=1
        except:
            continue
        else:
            continue
print(afabclist)
for i in range(n):
    mult=1
    for j in range(len(strlist[i])):
        tmp=abclist.index(strlist[i][j])#abclist에서 찾고
        sum=sum+afabclist[tmp]*mult#afabclist 값 대입
        mult*=10
print(sum)
                
