a=list(input())
stack=[0]
res=0
for i in range(len(a)):
    if(a[i]==')'):
        if(a[i-1]=='('):
            stack.pop()
            res+=sum(stack)

        else:
            stack.pop()
            res+=1
    else:
        stack.append(1)


print(res)
