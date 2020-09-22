def reverse(x):
    res=x[::-1]
    res=int(str(res))
    return res

def isPrime(x):
    cnt=0
    for i in range(1,x+1):
        if(x%i==0):
            cnt+=1
        if(cnt>2):
            return 0
    return 1
        
    
n=int(input())
a=input().split()
for i in range(len(a)):
    re_num=reverse(a[i])
    if(re_num!=1):
        res=isPrime(re_num)
        if(res):
            print(re_num,end=" ")
