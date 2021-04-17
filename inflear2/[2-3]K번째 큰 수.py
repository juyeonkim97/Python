n,k=map(int, input().split())
a=list(map(int,input().split()))
res=set()#중복 제거 자료구조
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for z in range(j+1,len(a)):
            res.add(a[i]+a[j]+a[z]) #append 아니고 add

#set은 sort 함수 없으니까 다시 리스트로 바꾸기
res=list(res)
res.sort()
print(res[-k])
