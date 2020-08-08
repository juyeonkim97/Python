#1082 16진수 구구단
n=input()    
for i in range(1,16):
    print("{}*{:X}={:X}".format(n,i,(int(n,16)*i)))
