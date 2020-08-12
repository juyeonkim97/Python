#1025 다섯 자리 정수 입력 받아 각 자리별로 나누어 출력
intlist=list(input())
intlistlen=len(intlist)
i=0
while(i<intlistlen):
    intlist[i]=int(intlist[i])
    i=i+1
multlist=[10000,1000,100,10,1]
i=0
while(i<intlistlen):
    print("[%d]"%(intlist[i]*multlist[i]))
    i=i+1
        
#1026 시분초 입력 받아 분만 출력
h,m,s=map(int,input().split(":"))
print(m)

#1027 년월일 입력 받아 일울년으로 출력
y,m,d=map(int,input().split("."))
print("%02d-%02d-%04d"%(d,m,y))

#1028
n=int(input())
print("%u"%n)
