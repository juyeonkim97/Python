#1061
a,b=map(int,input().split())
print(a|b)

#1062
a,b=map(int,input().split())
print(a^b)

#1063 3항 연산자 사용하여 두 수 중 큰 수 출력하기
a,b=map(int,input().split())
max=a if (a>b) else b
print(max)
