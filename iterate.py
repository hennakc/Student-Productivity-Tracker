#iterators and generators

lst=[10,20,30,40]
for i in lst:
    print(i)

ite=iter(lst)
print(ite.__next__()) #show elements one by one.
print(ite.__next__()) #second element shown.
print(ite.__next__()) #third element shown.
print(next(ite))