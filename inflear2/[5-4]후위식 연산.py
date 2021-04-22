a=list(input())
stack=list()
for i in a:

    if(i.isdecimal()):
        stack.append(i)
    else:
        num2=int(stack.pop())
        num1=int(stack.pop())
        if(i=="+"):
            stack.append(num1+num2)

        elif(i=="-"):
            stack.append(num1-num2)
        elif(i=="*"):
            stack.append(num1*num2)
        elif(i=="/"):
            stack.append(num1/num2)

print(stack.pop())
            
