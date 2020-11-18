 a=list(str(input()))
stack=list()
res=''
for i in range(len(a)):
    if(a[i] in ('0','1','2','3','4','5','6','7','8','9')):
        res+=a[i]
        print(res)
    elif(len(stack)==0):
        stack.append(a[i])
    elif(a[i]=='(' or a[i]=='*' or a[i]=='/'):
        stack.append(a[i])
        print(stack)
    elif(a[i]==')'):
        while(stack):
            if(stack[-1]=='('):
                stack.pop()
                print(stack)
            else:
                res+=stack.pop()
                print(stack)
    elif(a[i]=='+' or a[i]=='-'):
        if(stack[-1]=='*' or stack[-1]=='/'):
            while(stack):
                res+=stack.pop()
            stack.append(a[i])
            print(stack)
        else:
            stack.append(a[i])
            print(stack)
            
while(stack):
    res+=stack.pop()
print(res)
