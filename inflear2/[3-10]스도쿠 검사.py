def check(a):
    for i in range(9):
        ch=ch2=[0]*10
        for j in range(9):
            ch[a[i][j]]=1
            ch2[a[j][i]]=1
        if(sum(ch)!=9 or sum(ch2)!=9):
            return False
    #4중 for문 가능,,,
    for i in range(3):
        for j in range(3): #그룹 9개 보는 for문
            ch=[0]*10
            for z in range(3):#값 9개 보는 for문
                for q in range(3):
                    ch[a[i*3+z][j*3+q]]=1
            if(sum(ch)!=9):
                return False
    return True

a=[list(map(int,input().split())) for _ in range(9)]
if(check(a)):
    print("YES")
else:
    print("NO")
