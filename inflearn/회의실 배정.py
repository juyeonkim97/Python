n=int(input())
a=list()
for i in range(n):
    s,e=map(int,input().split())
    a.append((s,e))
a.sort(key=lambda x :(x[1],x[0]))#e로 정렬하게 하는 명령문,,정렬 우선순위 바꾼다
et=0
cnt=0
for s,e in a:
    if s>=et:
        cnt+=1
        et=e
print(cnt)
