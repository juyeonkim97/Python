#그리디 알고리즘
#백준 1744번

n=int(input())
A=list()
B=list()
res=list()#결과 리스트
for i in range(n):
    a=int(input())
    if(a<=0):#0포함 음수 리스트
        A.append(a) 
    elif(a==1):#1은 들어올 때부터 플러스 합 리스트에 넣기
        res.append(1)
    else:#양수 리스트
        B.append(a)
A.sort()
B.sort(reverse=True)#양수 리스트는 큰 순서대로
mult=1
for i in range(len(A)):
    if(len(A)%2==0):#갯수가 짝수이면 짝 묶어서 계속 곱하기
       if(mult==1):
           mult=mult*A[i]
       else:
           mult=mult*A[i]
           res.append(mult)
           mult=1
    else:#홀수면 마지막 하나 냅두고 짝 묶어서 계속 곱하기
       if(mult==1):
           mult=mult*A[i]
       else:
           mult=mult*A[i]
           res.append(mult)
           mult=1
       if(i==len(A)-1):
           res.append(A[i])
mult=1
for i in range(len(B)):
    if(len(B)%2==0):
       if(mult==1):
           mult=mult*B[i]
       else:
           mult=mult*B[i]
           res.append(mult)
           mult=1
    else:
       if(mult==1):
           mult=mult*B[i]
       else:
           mult=mult*B[i]
           res.append(mult)
           mult=1
       if(i==len(B)-1):
           res.append(B[i])     
print(sum(res))
