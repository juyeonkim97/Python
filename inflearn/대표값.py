n=int(input())
num=list(map(int,input().split()))
avg=int(float(sum(num)/n)+0.5)
gap=list()
for i in range(len(num)):
    gap.append(abs(avg-num[i]))
minindex=0
for i in range(len(num)):
    if(gap[minindex]>gap[i]):
        minindex=i
    elif(gap[minindex]==gap[i]):
        if(num[minindex]<num[i]):
            minindex=i
print(avg,minindex+1)
            
    
