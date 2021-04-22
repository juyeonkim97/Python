from collections import deque
n,m=map(int,input().split())
a=list(map(int,input().split()))

a.sort()
a=deque(a)
cnt=0

while(a):
    if(len(a)==1): #한명 남았을 경우 이 조건이 없으면 else문에서 오류남
        cnt+=1
        break
    if(a[0]+a[-1]>m):
        a.pop()
        cnt+=1
    else:
        a.popleft()#이 구문을 효율적으로 하기위해서 deque 자료구조 이용하기
        a.pop()
        cnt+=1
print(cnt)
