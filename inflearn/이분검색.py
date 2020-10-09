n,num=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
lt=0
rt=n-1
while(lt<=rt):
    mid=(lt+rt)//2
    if(a[mid]==num):
        break
    elif(a[mid]<num):
        lt+=1
    elif(a[mid]>num):
        rt-=1
    
print(mid+1)
