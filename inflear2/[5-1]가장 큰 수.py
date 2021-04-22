num,m=map(int,input().split())
num=list(str(num))
res=list()
i=0
while i<len(num):
    tmp=int(num[i])
    if(m!=0):
        if(len(res)==0):
            res.append(tmp)
            i+=1
        else:
            if res[-1]<tmp:
                res.pop()
                m-=1
            else:
                res.append(tmp)
                i+=1
    else:
        res.append(tmp)
        i+=1
if m!=0: 
    res=res[:-m]
for i in res:
    print(i,end="")
    
