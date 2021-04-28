import sys
def DFS(L):
    if(L==n):
        sum=0
        for j in range(n):
            sum+=p[j]*b[j]
        if(sum==f):
            for j in range(n):
                print(p[j],end=" ")
            sys.exit(0)
        
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1)#dfs 밑이 호출 후 되돌아 온 후에 지나가는 거
                ch[i]=0 #호출 후 되돌아 온 후 ch 풀어줘야 함....

n,f=map(int,input().split())
p=[0]*n #결과 담을 리스트
b=[1]*n #이항계수 만들어 놓을 리스트, 양끝은 1이니까 1로 초기화
ch=[0]*(n+1) #순열 담을 리스트
for i in range(1,n):#이항계수 만드는 반복문
    b[i]=b[i-1]*(n-i)//i
DFS(0)
    

     

