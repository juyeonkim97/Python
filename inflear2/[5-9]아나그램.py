a=input()
b=input()
aa=dict()
bb=dict()
for i in a:
    aa[i]=aa.get(i,0)+1 #aa[i]값이 있으면 그 값 없으면 0을 리턴
for i in b:
    bb[i]=bb.get(i,0)+1
for i in aa.keys():
    if i in bb.keys():#bb의 키값에 있냐
        if(aa[i]!=bb[i]):
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
    
##개선 코드
##a=input()
##b=input()
##sH=dict()
##for x in a:
##    sH[x]=sH.get(x, 0)+1
##for x in b:
##    sH[x]=sH.get(x, 0)-1
##
##for x in a:
##    if(sH.get(x)>0):
##        print("NO")
##        break;
##else:
##    print("YES")
