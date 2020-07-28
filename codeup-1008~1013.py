#1008 특수문자 유니코드 출력
#import io, sys
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
print('\u250C\u252C\u2510\n\u251C\u253C\u2524\n\u2514\u2534\u2518')

#1010 입력 받아서 출력
n=input()
print(n)

#1011
s=input()
print(s)

#1012 실수 입력 받아서 출력
f=float(input())
print("%f"%f)

#1013 정수 2개 입력 받아서 출력
a,b=map(int,input().split( ))
print("%d %d"%(a,b))
