a=list(str(input()))
stack=list()
res=''
for x in a:
    if(x.isdecimal()): #x가 숫자인지 확인 isdecimal() 메소드 사용
        res+=x
        print(res)
    else:
        if(x=='('):
            stack.append(x) #여는 괄호는 무조건 append
        elif(x=='*' or x=='/'):#곱하기 나누기인 경우
            while(stack and (stack[-1]=="*" or stack[-1]=="/")):
                res+=stack.pop() #pop과 res에 저장 동시
            stack.append(x)
        elif(x=="+" or x=="-"):#더하기 빼기인 경우
            while(stack and stack[-1]!="("): #여는 괄호 안에 있는 연산자 고려,여는 괄호 전까지 다 pop
                res+=stack.pop()
            stack.append(x)
        elif(x==")"): #닫는 괄호인 경의
            while(stack and stack[-1]!="("): #여는 괄호 전까지 pop
                res+=stack.pop()
            stack.pop() #여는 괄호 pop, 저장은 하지 않
                 
while(stack):
    res+=stack.pop()
print(res)
