s=list(input())
res=0
for i in s:
    if i.isdecimal():
        res=res*10+int(i)

print(res)
cnt=1
for i in range(2,res+1):
    if(res%i==0):
        cnt+=1
print(cnt)
