from collections import deque
s,e=map(int,input().split())
max=10000
min=2147000000
dis=[0]*(max+1)
ch=[0]*(max+1)
dis[s]=0
ch[s]=1
dq=deque()
dq.append(s)
while dq:
    now=dq.popleft()
    if now==e:
        break
    for next in (now-1,now+1,now+5): #저 세 값들 한 번씩 할당 받으면서 세번 반복됨
        if 0<next<=max:
            if(ch[next]==0):
                dq.append(next)
                ch[next]=1
                dis[next]=dis[now]+1
print(dis[e])
