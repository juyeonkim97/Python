#그리디 알고리즘
#백준 1946번

import sys
def interview():
    n=int(sys.stdin.readline())
    alist=list()
    for j in range(n):
        a,b=map(int,sys.stdin.readline().split())
        alist.append((a,b))
    alist=sorted(alist,key=lambda alist:alist[0])
    z=1
    j=0
    passcon=1
    cnt=n
    while(z!=n):
        if alist[z][1]>alist[j][1]:
                passcon=0
                cnt-=1
        if j!=z and passcon!=0:
            j+=1
        else:
            z+=1
            j=0
            passcon=1
    return cnt

t=int(sys.stdin.readline())
for i in range(t):
    cnt=interview()
    print(cnt)
        
