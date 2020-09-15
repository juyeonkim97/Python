#그리디 알고리즘
#백준 1700번

n,k=map(int,input().split())#구멍 개수, 사용 횟수
a=list(map(int,input().split()))
con=list()
cnt=0
for i in range(len(a)):
    if(a[i] not in(con)):
        if(len(con)!=n):
            con.append(a[i])
        else:
            index=0
            for j in range(i+1,len(a)):
                if(a[j] in(con)):
                    index=con.index(a[j])
                else:
                      
            cnt+=1
            con[index+1]=a[i]
    print(con)
print(cnt)
