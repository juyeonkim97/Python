from collections import deque
n,k=map(int,input().split())
a=[ i for i in range(1,n+1)]
a=deque(a)
while len(a)!=1:
    for i in range(k-1):
        a.append(a.popleft())
    a.popleft()
print(a[0])
    
