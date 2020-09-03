#그리디 알고리즘
#백준 1783번

n,m=map(int,input().split())
loc=[n-1,0]#위치, 처음 위치
cnt=1#처음 위치까지 세는 거임
if(n==1 or m==1):
    cnt=1
elif(n<=2 or m<=6):
    while(True):
        if(cnt==4):
           break
        if(loc[0]-2>=0):
            loc[0]-=2
            loc[1]+=1
            if(loc[1]>m-1):
                break
            cnt+=1
        elif(loc[0]+2<=n-1):
            loc[0]+=2
            loc[1]+=1
            if(loc[1]>m-1):
                break
            cnt+=1
        elif(loc[0]-1>=0):
            loc[0]-=1
            loc[1]+=2
            if(loc[1]>m-1):
                break
            cnt+=1
        elif(loc[0]+1<=n-1):
            loc[0]+=1
            loc[1]+=2
            if(loc[1]>m-1):
                break
            cnt+=1
        else:
            break
else:
    cnt=m-2    
print(cnt)
