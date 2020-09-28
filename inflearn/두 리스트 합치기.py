n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))
C=list()
p1=0
p2=0
while p1<n and p2<m:#둘 다 해당하는 동안 돌아간다 이얘기
    #하나라도 끝까지 가면 멈춘다는 얘기
    if(A[p1]<=B[p2]):
        C.append(A[p1])
        p1+=1
    else:
        C.append(B[p2])
        p2+=1
        
if p1<n:#p2가 끝까지 간 경우
    C=C+A[p1:]
else:
    C=C+B[p2:]
    
for i in C:
    print(i,end=" ")
        
