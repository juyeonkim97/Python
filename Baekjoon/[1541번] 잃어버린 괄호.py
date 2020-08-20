#그리디 알고리즘
#백준 1541번

a=input()
eq=list()
tmp=""
minus=list()
for i in range(len(a)):
    if a[i]=="-":
        eq.append(int(tmp))
        eq.append("-")
        tmp=""
    elif a[i]=="+":
        eq.append(int(tmp))
        tmp=""
    else:
        tmp+=(a[i])
eq.append(int(tmp))
check=list()#마이너스 연산자의 위치를 저장하는 리스트
for i in range(len(eq)):
    if eq[i]=="-":
        check.append(i)

if len(check):#check리스트가 비어있지 않다면
    first_sum=sum(eq[0:check[0]])#마이너스 연산자가 나오기 전까지 더한 값
    for i in range(len(check)):
        if i+1 < len(check):
            first_sum-=sum(eq[check[i]+1:check[i+1]])
        else:
            first_sum-=sum(eq[check[i]+1:])
    print(first_sum)
else:#check 리스트가 빈 경우=마이너스 연산자가 없는 식
    print(sum(eq))
