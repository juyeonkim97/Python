def reverse(x):
    x=list(x)
    x=x[::-1]#리스트 뒤집기(리스트 역순)
    return x

def isPrime(x):
    i=0
    cnt=0
    for i in range(2,x+1):
        if(x%i==0):
            cnt+=1
    if cnt==1:
        return 1
    else:
        return 0
    
n=int(input())
a=input().split()
for i in a:
    x=reverse(i)
    x=int("".join(x))
    res=isPrime(x)
    if(res==1):
        print(x,end=" ")
    
