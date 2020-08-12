#1073
l=input().split()
for x in l:
    if x!='0':
        print(x)
    else:
        break

#1074
n=int(input())
while(n>0):
    print(n)
    n=n-1

#1075
n=int(input())
n=n-1
while(n>=0):
    print(n)
    n=n-1

#1076 문자 1개 입력받아 알파벳 출력하
a=ord(input())
i=ord('a')
while(i<=a):
    print("%c"%i,end=" ")
    i=i+1

#1077
n=int(input())
for i in range(n+1):
    print(i)
