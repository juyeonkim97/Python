def DFS(L,P):
    global cnt
    if(L==n):
        for i in range(P): #range(P)라고 하면 res 초기화하는 과정 없이 가능
            print(chr(64+res[i]),end="")
        print()
        cnt+=1
        
    else:
        for i in range(1,27):
            if(code[L]==i):
                res[P]=i
                DFS(L+1,P+1)
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                res[P]=i
                DFS(L+2,P+1)
                
            
            
            
code=list(map(int,input())) #문자열 하나씩 숫자로 바꿔서 리트스화
n=len(code)
code.insert(n,-1) #out of range 방지
res=[0]*(n*3)
cnt=0
DFS(0,0)
print(cnt)
