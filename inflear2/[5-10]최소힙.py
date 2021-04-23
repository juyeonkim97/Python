import heapq as hq #최소힙을 구현해주는 라이브러리
a=list()
while True:
    tmp=int(input())
    if(tmp==0):
        if(len(a)==0):
            print(-1)
        else:
            print(hq.heappop(a)) #루트 노드 값 출력 => 최소값 출력
    elif(tmp==-1):
        break
    else:
        hq.heappush(a,tmp) #a라는 리스트에 tmp 넣어라
        
        
    
