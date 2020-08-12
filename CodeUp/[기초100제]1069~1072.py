#1069
a=input()
if a=="A":
    print("best!!!")
elif a=="B":
    print("good!!")
elif a=="C":
    print("run!")
elif a=="D":
    print("slowly~")
else:
    print("what?")

#1070
a=int(input())
if a==12 or a==1 or a==2:
    print("winter")
elif a==3 or a==4 or a==5:
    print("spring")
elif a==6 or a==7 or a==8:
    print("summer")
else:
    print("fall")

#1071
list=input().split()
for i in list:
    i=int(i)
    if i==0:
        break
    else:
        print(i)

#1072
n=int(input())
m=input().split()
for i in m:
    print(i)
