#1088
a=int(input())
for i in range(1,a+1):
    if(i%3==0):
        continue
    else:
        print(i,end=" ")

#1089
a,d,n=map(int,input().split())
result=a
for i in range(2,n+1):
    result+=d
print(result)

#1090
a,m,d,n=map(int,input().split())
result=a
for i in range(2,n+1):
    result=result*m+d
print(result)

#1092 세 수의 최소공배수 구하기
a,b,c=map(int,input().split())
day=1
while(day%a!=0 or day%b!=0 or day%c!=0):
    day=day+1
print(day)

#1093
n=int(input())
num=list(map(int,input().split()))
cnt=list()
for i in range(1,24):
    cnt.append(num.count(i))
    print(cnt[i-1],end=" ")



