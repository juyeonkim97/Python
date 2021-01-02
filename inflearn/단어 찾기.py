n=int(input())
p=dict() #빈 딕셔너리 생성
for i in range(n):
    word=input()
    p[word]=1 #word를 키값으로, 1을 value로
for i in range(n-1):
    word=input()
    p[word]=0 #사용된 단어는 word 인덱스의 값을 0으로 변경
for key, val in p.items(): #딕셔너리 내용물에 접근하는 법 p.items()
    if(val==1):
        print(key)
        break
 
