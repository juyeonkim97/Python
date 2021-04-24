import sys
def DFS(L,sum):
    if sum>total//2:#조금 더 빨리 끝내기 위해
        return #함수 종료, 가지를 하나 없애는 거 뿐임
    if(L==n):
        if(sum==total-sum):
            print("YES")
            sys.exit(0) #함수 종료 아니고 프로그램 종료,import 필요
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)
        

n=int(input())
a=list(map(int,input().split()))
total=sum(a)
DFS(0,0)
print("NO")
