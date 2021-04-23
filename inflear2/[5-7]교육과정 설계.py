from collections import deque
ok=list(input())
n=int(input())
for i in range(n):
    a=input()
    tmp=ok
    tmp=deque(tmp)
    for j in a:
        if j in tmp:
            if j!=tmp.popleft():#테스트 5 위한 조건
                print("#%d NO"%(i+1))
                break
            #else 구문 없어도 popleft()는 실행이 되는 거임,,,,if문 확인하면서..
    else:
        if(len(tmp)==0):
            print("#%d YES"%(i+1))
        else:
            print("#%d NO"%(i+1))
    
