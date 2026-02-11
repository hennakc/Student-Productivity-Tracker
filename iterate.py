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
    def __init__(self,max):
        self.num=1
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=self.max:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
c=Count(3)
print(c.__next__()) #object is iterable.
print(c.__next__()) #first element shown.#ticketbooking system and hotel booking system are examples of iterators.
        
 
#GENERATORS:
#it can be used to create iterators in a simple way. It uses yield keyword instead of return keyword. It can be used to generate infinite sequence of numbers.
def display(n):
    for i in range(3):
        yield i  #one value is only retrieved at a time. It will return a generator object.
d=display(3)
print(d.__next__()) #it will return a generator object.
#print(d.__next__())

#function inside functions

def display1():
    def display2():
        print("this is function display2 inside display1")
    display2();

display1();
    

