#그리디 알고리즘
#백준 1449번

n,l=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
cnt=1
loc=a[0]-0.5+l
for i in a:
    if(loc>=i+0.5):
        continue
    else:
        loc=i-0.5+l
        cnt+=1
print(cnt)    
