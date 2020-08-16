#그리디 알고리즘
#백준 1931번

n=int(input())
s=[0]*n #시작 시간 리스트
e=[0]*n #끝나는 시간 리스트
for i in range(n):
    s[i],e[i]=list(map(int,input().split()))

for i in range(n):
    for j in range(n):
        if((a[i]+1) == s[j]):
            i= j
            cnt+=1
            
