#그리디 알고리즘
#백준 1541번

a=list(input())
minus=list()
plus=list()
summinus=0
minuscnt=0 #빼기를 기준으로 수식을 나눌 거임
minuslist=list()
for i in range(len(a)):
    if(a[i]=="-"):
        minuscnt+=1
        for j range(i):
            minus.append(a[j])#빼기 앞에 있는 수 저장
            summinus-=int(minus))#정수로 바꿔서
            minuslist.append(summinus)
        minus.clear()
