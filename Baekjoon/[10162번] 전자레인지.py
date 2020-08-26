#그리디 알고리즘
#백준 10162번

import sys
t=int(sys.stdin.readline())
res=0
for i in range(int(t/10)+1):
    for j in range(int(t/60)+1):
        for z in range(int(t/300)+1):
            if ((z*300+j*60+i*10) == t):
                print(z,j,i)
                res=1
        if(res==1):
            break
    if(res==1):
            break
if res==0:
    print(-1)
