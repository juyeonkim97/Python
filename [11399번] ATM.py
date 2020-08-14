n=int(input())
p=list(map(int,input().split()))
p.sort()
wait=0
sum=0
for i in p:
    wait+=i
    sum+=wait
print(sum)
