from collections import deque
need=input()
n=int(input())
for i in range(n):
    plan=input()
    dq=deque(need)
    for x in plan:
        if x in dq :
            if x!=dq.popleft():
                print("#%d NO"%(i+1))
                break
    else: #끝까지 통과한 것, 하지만 한 가지 더 검사해야됨
        if len(dq)==0 : #0이 아니라는 건 필수과목 뺀 게 있다는 것
            print("#%d YES"%(i+1))
        else:
            print("#%d NO"%(i+1))
