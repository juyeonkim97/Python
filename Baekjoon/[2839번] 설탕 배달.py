#그리디 알고리즘
#백준 2839번

n=int(input())
a=[5,3]
cnt=0
if(n==4):
    cnt=-1
elif(n<3):
    cnt=n-3
for i in a:
    tmp=int(n/i)
    cnt=cnt+tmp
    n=n%i
    print(tmp,cnt,n)#몫, 몫을 더한 값, 나머지
    if(n==0):
        break
    elif((n/3)<1):
        cnt=cnt+1
print(cnt)


