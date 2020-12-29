from collections import deque
n,m=map(int,input().split())
Q=[(pos,val) for pos,val in enumerate(list(map(int,input().split())))]
#인덱스와 위험도 짝인 튜플 생성
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft() #튜플 반환됨
    if(any(cur[1]< x[1] for x in Q)): #[1]을 써야됨, 튜플 cur은 튜플이니까
       Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break
