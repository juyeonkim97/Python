from collections import deque
n=int(input())
a=[input() for _ in range(n)]
b=[input() for _ in range(n-1)]
a.sort()
b.sort()
a=deque(a)
b=deque(b)
while b:
    tmp=a.popleft()
    tmp2=b.popleft()
    if(tmp==tmp2):
        continue
    else:
        a.append(tmp)
        b.insert(0,tmp2)
print(a[0])
    
