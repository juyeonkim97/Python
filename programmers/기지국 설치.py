#효율성 0점!!!!!!
def solution(n, stations, w):
    answer = 3
    a=[0]*(n+1)
    cnt=0
    for i in stations:
        j=i-w
        for j in range(i-w,i+w+1):
            if(j>=1 and j<=n):
                a[j]=1
    
    p=2
    tmp=0
    for i in range(1,n+1):
        if a[i] != p: 
            p=a[i]
            tmp2=tmp//(w*2+1)
            tmp3=tmp%(w*2+1)
            if(tmp3!=0 and i!=0 and p==1):
                cnt+=1
            if(p==1):
                cnt+=tmp2
            tmp=1
        else:
            tmp+=1
        
    if(p==0): #계속 0인 경우에서 끝난 경우
        tmp2=tmp//(w*2+1)
        tmp3=tmp%(w*2+1)
        if(tmp3!=0 and i!=0):
            cnt+=1
        cnt+=tmp2
        
    answer=cnt
    return answer
