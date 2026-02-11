#lamda functions

#normal function
def cal(a,b,c):
    d=a+b+c
    return d;
res=cal(10,20,30)
print(res);

#using lambda
res1=lambda a,b,c : a+b+c; #lamda function is used to create anonymous functions. It can take any number of arguments but can only have one expression. It is used for short and simple functions.
print(res1(10,20,30)) #cant be used if more than one expression is there. It is used in filter, map and reduce functions. It is also used in sorting and other functions where a function is required as an argument.


#inside functions:
def calc1():
    ld=lambda a,b : a*b
    return ld(10,20)
print(calc1())  #n number of variables and one expression.

#map functions accept lamda functions

lst=[10,20,30,40]
#output=[110,120,130,140]

lst1=list(map(lambda x:x+100,lst)) #(lambda variables:expression,source)
print(lst1)

lst3=[10,13,14,17,16];
lst4=list(filter(lambda x:x%2==0,lst3))
print(lst3)
print(lst4)