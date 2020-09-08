#그리디 알고리즘
#백준 4796번

def camping(L,P,V):
    if(V%P <= L):  
        res=V//P*L+V%P #// 하면 몫만 나옴
    else:
        res=V//P*L+L
    return res

L,P,V=map(int,input().split())
i=1
while(L!=0):
    res=camping(L,P,V)
    print("Case {}: {}".format(i,res))
    L,P,V=map(int,input().split())
    i+=1
