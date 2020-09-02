#그리디 알고리즘                   
#백준 1138번

def cntcheck(i):
    cnt=0
    for j in b:
        if(i<j):
            cnt+=1
        if(i==j):
            break
    return cnt

def movenum(i):
    cnt=cntcheck(i)
    while(cnt!=a[i-1]):
        tmp=b.index(i)
        b[tmp]=b[tmp-1]
        b[tmp-1]=i
        cnt=cntcheck(i)
        
n=int(input())
a=list(map(int,input().split()))
b=list()
for i in range(n,0,-1):
    b.append(i)
    cnt=cntcheck(i)
    if(cnt!=a[i-1]):
        movenum(i)
for i in b:
    print(i,end=" ")
