n=int(input())
part=list()
res=list()
for i in range(n):
    partset=set()#초기화,,
    a,b,c=map(int,input().split())
    partset.add(a)
    partset.add(b)
    partset.add(c)
    part=list(partset)
    cnt=len(part)
    if(cnt==1):#세개가 같은 눈
        res.append(10000+a*1000)
    elif(cnt==2):#두개가 같은 눈
        if(a==b):
            res.append(1000+b*100)
        elif(a==c):
            res.append(1000+c*100)
        else:
            res.append(1000+b*100)
    else:#다 다른 눈
        tmp=max(part)
        res.append(tmp*100)
print(max(res))

