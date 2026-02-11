import copy
lst=[
    [10,20,30],
    [40,50,60],
]
lst1=copy.copy(lst)
lst1[0][0]=100
print(lst)
print(lst1)