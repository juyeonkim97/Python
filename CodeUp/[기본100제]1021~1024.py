#1021
str=input()
print("%s"%str)

#1022
str=input()
print("%s"%str)

#1023 실수 입력 받아 정수부, 실수부 출력
d,f=map(int,input().split('.'))
print("%d\n%d"%(d,f))

#1024
strlist=list(input())
i=0
while(i<len(strlist)):
    print("\'%s\'"%strlist[i])
    i=i+1
