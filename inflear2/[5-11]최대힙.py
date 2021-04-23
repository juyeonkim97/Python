import heapq as hq 
a=list()
while True:
    tmp=int(input())
    if(tmp==0):
        if(len(a)==0):
            print(-1)
        else:
            print(-(hq.heappop(a)))
    elif(tmp==-1):
        break
    else:
        hq.heappush(a,-(tmp))
