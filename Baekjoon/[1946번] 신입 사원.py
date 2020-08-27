#그리디 알고리즘
#백준 1946번

import sys
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    cnt=1#서류 성적 1위는 무조건 카운트하고
    alist=list()
    for j in range(n):
        a,b=map(int,sys.stdin.readline().split())
        alist.append((a,b))
    alist=sorted(alist,key=lambda alist:alist[0])
    tmp=alist[0][1]
    for z in range(len(alist)):
        if alist[z][1] < tmp:
            cnt+=1
            tmp=alist[z][1]
            if(tmp==1):
                break
    print(cnt)
