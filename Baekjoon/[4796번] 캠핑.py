#그리디 알고리즘
#백준 4796번

def camping(L,P,V):
    res=int(V/P)*L+(V%P)
    return res

L,P,V=map(int,input().split())
i=1
while(L!=0):
    res=camping(L,P,V)
    print("Case {}: {}".format(i,res))
    L,P,V=map(int,input().split())
    i+=1
