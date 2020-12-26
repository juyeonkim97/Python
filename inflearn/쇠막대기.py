a=list(str(input()))
stack=list()
res=0
for i in range(len(a)):
    if(a[i]=='('): #여는 괄호면 무조건 append
        stack.append(a[i])
    elif(a[i]==')'): #닫는 괄호면 앞을 확인
        if(a[i-1]=='('): #앞에 있는 건 a[i-1]
            stack.pop()
            res+=len(stack) 
        else:
            stack.pop()
            res+=1
print(res)
