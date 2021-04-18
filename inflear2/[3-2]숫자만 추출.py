n=list(input())
num=list()
for i in n:
    if(i>='0' and i<='9'): #숫자인지 판별
       num.append(i)
num="".join(num)
num=int(num)
cnt=0
for i in range(1,num+1):
    if(num%i==0):
        cnt+=1
print(num,cnt)
    

