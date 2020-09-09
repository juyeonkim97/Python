#그리디 알고리즘
#백준 2437번

import sys
n=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
A.sort()
sum=0
for i in range(len(A)):
    if sum+1 >= A[i]:
        sum+=A[i]
    else:
        break
print(sum+1)
