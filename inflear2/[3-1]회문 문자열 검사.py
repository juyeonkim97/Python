n=int(input())
for i in range(n):
    a=list(input().lower())
    if(a[::-1]==a):
        print("#%d YES"%(i+1))
    else:
        print("#%d NO"%(i+1))
