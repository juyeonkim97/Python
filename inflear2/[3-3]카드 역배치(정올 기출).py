a=[i for i in range(21)] #리스트 1-20까지 초기화
for i in range(10):
    ai,bi=map(int,input().split())
    s=a[ai:bi+1]
    a[ai:bi+1]=s[::-1]
for i in range(1,21):
    print(a[i],end=" ")
    
