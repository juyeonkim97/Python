#그리디 알고리즘
#백준 1946번

import sys
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    cnt=n
    alist=list()
    for j in range(n):
        a,b=map(int,sys.stdin.readline().split())
        alist.append((a,b))
        alist=sorted(alist,key=lambda alist:alist[0])
    for z in range(1,len(alist)):#1위는 어쨌든 하나라도 이겼으니까 볼 필요 없음
        for j in range(z):#z가 1일때, 순위는 2위 비교대상은 인덱스 0인 1위
            if alist[z][1]>alist[j][1]:
                cnt-=1
                break
    print(cnt)
        
