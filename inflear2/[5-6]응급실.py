from collections import deque
n,m=map(int, input().split())
eme=list(map(int,input().split()))
a=list()
for i in range(n):
    a.append((eme[i],i))
a=deque(a)
i=0
while a:
    if(a[0][0]<max(a)[0]):
        a.append(a.popleft())
    else:
        i+=1
        if(a[0][1]==m):
            print(i)
            break
        else:
            a.popleft()
