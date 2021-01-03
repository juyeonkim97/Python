#아나그램 해쉬 이용
a=input()
b=input()
sH=dict()
for x in a:
    sH[x]=sH.get(x,0)+1 #get(x,0)은 x라는 키값이 없으면 0을 value로 한다는 말
for x in b:
    sH[x]=sH.get(x,0)-1 #b를 받아서 value 값 다시 -1 한다

for x in a:
    if(sH[x]>0): #위에 과정을 해서 아나그램이라면 모든 value는 0이어야 함
        print("NO")
        break
else: #for else 구문, else문은 모든 반복을 무사히 마쳤을 때 실행되는 것
    print("YES")
