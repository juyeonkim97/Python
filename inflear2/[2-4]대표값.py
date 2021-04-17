n=int(input())
a=list(map(int,input().split()))
mean=round(sum(a)/n) #첫째자리 반올림, 평균 내기
min=2147000000
for idx,x in enumerate(a): #인덱스와 값을 쌍을 지어주는 함수
    tmp=abs(x-mean)
    if(tmp<min):
        min=tmp
        score=x
        res=idx+1
    elif(tmp==min):
        if(x>score):
            score=x
            res=idx+1
        
print(mean,res)
