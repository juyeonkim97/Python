#그리디 알고리즘
#백준 5585번

m=[500,100,50,10,5,1]
n=1000-int(input())
cnt=0
for i in m:
    while(n>=i):
        cnt+=int(n/i)
        n=n%i
        if(n==0):
            print(cnt)
            break
