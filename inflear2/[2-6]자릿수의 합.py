def digit_sum(x):
    ds=0
    x=list(x) #문자열 리스트로 바꾸기
    for i in x:
        ds+=int(i)
    return ds

n=int(input())
a=input().split()
max=-2147000000
for i in a:
    tmp=digit_sum(i)
    if(max<tmp):
        max=tmp
        res=i
print(res)
