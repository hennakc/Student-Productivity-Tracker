#iterators and generators

lst=[10,20,30,40]
for i in lst:
    print(i)

ite=iter(lst)
print(ite.__next__()) #show elements one by one.
print(ite.__next__()) #second element shown.
print(ite.__next__()) #third element shown.
print(next(ite))

#custom iteration:

class Count:                   #use three functions to create an iterator.
    def __init__(self):
        self.num=1
        self.max=0
    def __iter__(self):
        return self
    def __next__():
        if self.num<=self.max:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
        
 
