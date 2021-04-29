import itertools as it
n, f=map(int, input().split())
b=[1]*n
cnt=0
for i in range(1, n):#이항계수
    b[i]=b[i-1]*(n-i)/i
a=list(range(1, n+1))
for tmp in it.permutations(a):#순열 만들어주는 라이브러리 (a,n)하면 n개만 뽑아서 순열
    sum=0
    for L, x in enumerate(tmp):#인덱스-값 조합 딕셔너리 리턴해주는 함수
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break
