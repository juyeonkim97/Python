#그리디 알고리즘
#백준 2217번

import sys
n=int(sys.stdin.readline())
sum=0
a=list()
for i in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()
maxlist=list()
for i in range(len(a)):
    maxlist.append(a[i]*(n-i))
print(max(maxlist))
