num,m=map(int,input().split())
num=list(map(int,str(num))) #str(num) 해야 num이 하나 하나 리스트로 들어감
stack=list()
for i in num:
    while stack and stack[-1]<i and m>0 : 
        m-=1
        stack.pop()
    stack.append(i)
    
if(m!=0):
    stack=stack[:-m] #5개 버려야 되는데 3개만 버려서 2개 남은 경우, 리스트 뒤에 두개 버리는 법
for j in stack:
    print(j,end="")
