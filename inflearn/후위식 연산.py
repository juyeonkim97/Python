a=list(input())
stack=list()
for i in range(len(a)):
    if a[i].isdecimal() :
        stack.append(int(a[i])) #문자는 숫자로 변환해서 넣
    else:
        n1=stack.pop() 
        n2=stack.pop()
        if(a[i]=="*"): 
            stack.append(n2 * n1) #먼저 pop된 게 뒤에 있는 피연산자가 돼야함
        elif(a[i]=="/"):
            stack.append(n2 /  n1)
        elif(a[i]=="+"):
            stack.append(n2 + n1)
        elif(a[i]=="-"):
            stack.append(n2 - n1)
print(stack[-1])
