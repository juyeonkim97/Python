from collections import deque
n=int(input())
a=list(map(int,input().split()))

tmp=list()
res=""#이렇게 하면 문자열이고 +해서 저장하면 바로 출력 가능
tmp=list()
fin=0
lt=0
rt=n-1
while lt<=rt:
    if(fin<a[lt]):
        tmp.append((a[lt],"L"))
    if(fin<a[rt]):
        tmp.append((a[rt],"R"))
    tmp.sort()
    
    if(len(tmp)==0):
        break
    else:
        res+=tmp[0][1]
        fin=tmp[0][0]  
        if(tmp[0][1]=="L"):
            lt+=1
        else:
            rt-=1

    tmp.clear()
print(len(res))
print(res)
