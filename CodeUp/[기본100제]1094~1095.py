#1094
n=int(input())
num=list(map(int,input().split()))
num.reverse()
for i in range(len(num)):
    print(num[i],end=" ")

#1095
n=int(input())
num=list(map(int,input().split()))
num.sort()
print(num[0])
