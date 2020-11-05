from collections import deque
n=int(input())
a=list(map(int,input().split()))
a=deque(a)
cd=0
lrstr=""
for i in range(n-1):
    if(len(a)==1 and a[0]>cd):
        lrstr+="L"
    if(a[0]>cd and a[-1]>cd):
        if(a[0]< a[-1]):
            cd=a[0]
            a.popleft()
            lrstr+="L"
        else:
            cd=a[-1]
            a.pop()
            lrstr+="R"
    else:
        if(a[0]>cd):
            cd=a[0]
            a.popleft()
            lrstr+="L"
        else:
            cd=a[-1]
            a.pop()
            lrstr+="R"
print(len(lrstr))
print(lrstr)
