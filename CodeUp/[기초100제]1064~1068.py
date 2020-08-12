#1064
a,b,c=map(int,input().split())
max=(a if a<b else b) if (a if a<b else b) <c else c
print(max)

#1065
a,b,c=map(int,input().split())
for i in a,b,c:
    if i%2==0:
        print(i)
        
#1066
a,b,c=map(int,input().split())
for i in a,b,c:
    if i%2==0:
        print("even")
    else:
        print("odd")

#1067
a=int(input())
if a>0:
    print("plus")
else:
    print("minus")

if a%2==0:
    print("even")
else:
    print("odd")

#1068 
a=int(input())
if a>=90 and a<=100:
    print("A")
elif a>=70 and a<=89:
    print("B")
elif a>=40 and a<=69:
    print("C")
elif a>=0 and a<=39:
    print("D")
    
