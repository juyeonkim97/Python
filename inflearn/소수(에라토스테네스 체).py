#에라토스테네스 체
n=int(input())
cnt=0
ch=[0]*(n+1)
for i in range(2,n+1):
    if(ch[i]==0):
        cnt+=1
        for j in range(i,n+1,i):#스텝 지정
            ch[j]=1
print(cnt)
