a=list(str(input()))
stack=list()
res=0
for i in range(len(a)):
    if(a[i]=='('):
        stack.append(a[i])
    elif(a[i]==')'):
        if(a[i-1]=='('):
            stack.pop()
            res+=len(stack)
        else:
            stack.pop()
            res+=1
print(res)
            
