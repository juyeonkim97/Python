from collections import deque
n,k=map(int,input().split())
dq=list(range(1,n+1)) #1부터 n까지의 리스트 만드는 법
dq=deque(dq)
while(len(dq)!=1):
    for _ in range(k-1):
        dq.append(dq.popleft())
    dq.popleft()
print(dq[0])
