print("enter two numbers")
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("1.add 2.substraction 3.multiplcation 4.division")
c=int(input())
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
else:
    print(a/b)