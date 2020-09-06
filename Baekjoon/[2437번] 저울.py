#그리디 알고리즘
#백준 2437번

import sys
n=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
A.sort()
num=1
con=True
while(con):
    tmp=num
    for i in range(len(A)):
        if(A[i]>=num):
            index=i
            break
    for i in range(index,-1,-1):
        if(A[i]<=tmp):
            tmp=tmp-A[i]
        if(tmp==0):
            num+=1
            break
        elif(i==0 and tmp!=0):
            con=False
            break
print(num)
    
