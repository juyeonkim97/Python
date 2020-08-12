#1036 영문자 입력 받아 10진수로 출력
a=str(input())
a=ord(a)
print("%d"%a)

#1037 정수 입력 받아 아스키 문자로 출력
a=int(input())
a=chr(a)
print("%c"%a)

#1038
a,b=map(int,input().split())
print("%d"%(a+b))

#1039
a,b=map(int,input().split())
print("%ld"%(a+b))

#1040
a=int(input())
print("%d"%-a)

#1041
a=ord(input())
print("%c"%(a+1))

#1042
a,b=map(int,input().split())
print("%d"%(a/b))
