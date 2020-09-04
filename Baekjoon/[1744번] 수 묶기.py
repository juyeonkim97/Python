#그리디 알고리즘
#백준 1744번

n=int(input())
A=list()
for i in range(n):
    a=int(input())
    A.append(a)
A.sort(reverse=True)
res=list()#결과 리스트
mult=1
for i in range(len(A)):
    if(A[i]<0):#음수가 연달아 세개 나올 경우
        if(A[i-1]<=0):
            if(mult==1):
                mult=mult*A[i]
            else:
                mult=mult*A[i]
                res.append(mult)
                mult=1
        else:
            res.append(A[i])
    elif(A[i]==1):
        res.append(A[i])
    elif(A[i]>0 and (i!=n-1 and A[i-1]!=1)):
        if(mult==1):
            mult=mult*A[i]
        else:
            mult=mult*A[i]
            res.append(mult)
            mult=1
    else:
        res.append(A[i])
    print(res)
print(sum(res))
