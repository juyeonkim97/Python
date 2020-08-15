#그리디 알고리즘
#백준 11399번

n=int(input())
p=list(map(int,input().split()))
p.sort()
wait=0
sum=0
for i in p:
    wait+=i
    sum+=wait
print(sum)
