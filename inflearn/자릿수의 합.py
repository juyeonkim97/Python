def digit_sum(x):
    res=0
    while(x>0):
        res+=x%10
        x=x//10
    return res


n=int(input())
num=list(map(int,input().split()))
sumlist=list()
maxres=0
maxindex=0
for i in num:
    tmp=digit_sum(i)
    if(maxres<tmp):
        maxres=tmp
        res=i
print(res)
    
