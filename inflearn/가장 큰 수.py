num,m=map(int,input().split())
num=list(map(int,str(num)))
stack=list()
for i in num:
    while stack and stack[-1]<i and m>0 :
        m-=1
        stack.pop()
    stack.append(i)
    
if(m!=0):
    stack=stack[:-m]
for j in stack:
    print(j,end="")
    
    
