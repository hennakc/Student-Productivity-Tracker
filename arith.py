option="yes"
while(option=="yes"):
    print("enter two numbers")
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print("1.add 2.substraction 3.multiplcation 4.division 5.exit")
    c=int(input())
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
    elif c==4:
        if b==0:
            print("not divisible by 0")
        else:
            print(a/b)
    else:
        break
option=input("do u want to continue yes/no)")


    
