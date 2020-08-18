#그리디 알고리즘
#백준 1931번

import sys
n=int(sys.stdin.readline())
a=list()
cnt=0
for i in range(n):
    s,e=map(int,sys.stdin.readline().split())
    a.append((s,e))

a=sorted(a, key=lambda a:a[0])
a=sorted(a, key=lambda a:a[1])

s_time=0
for time in a:
    if time[0]>=s_time:
        s_time=time[1]
        cnt+=1
print(cnt)
