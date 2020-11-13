n=int(input())
a=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]
while(lt<=rt):
    if a[lt]>last:
        tmp.append((a[lt],'L'))
    if (a[rt]>last):
        tmp.append((a[rt],'R'))
    tmp.sort() #튜플의 첫번째 값으로 정렬
    if(len(tmp)==0): #리스트에 값이 없다는 건 둘 다 last보다 작음
        break
    else:
        res=res+tmp[0][1] #작은 값에 해당하는 스트링
        last=tmp[0][0]
        if(tmp[0][1]=='L'): #작은 값이 왼쪽인 경우
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(len(res))
print(res)
