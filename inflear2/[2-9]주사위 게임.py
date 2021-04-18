n=int(input())
res=list()
for i in range(n):
    a=list(map(int,input().split()))
    ch=[0]*7
    idx=10
    for j in a:
        ch[j]+=1
        if(max(ch)<ch[j]):
            idx=j
    if(idx==10):#모두 1인 경우
        idx=max(a)
    if(max(ch)==3):
        res.append(10000+idx*1000)
    elif(max(ch)==2):
        res.append(1000+idx*100)
    else:
        res.append(idx*100)
print(max(res))
        
    
