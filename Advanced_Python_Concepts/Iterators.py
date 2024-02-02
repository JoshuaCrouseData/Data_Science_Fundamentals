'''
Iterators are objects that can be iterated upon. In Python, 
an iterator implements two special methods, __iter__() and __next__(), 
collectively known as the iterator protocol.

Create a custom iterator that returns numbers, 
starting with 1, and each sequence will increase by one(1,2,3,...)
'''

class SimpleCounter:
    
    def __init__(self, limit):
        self.limit = limit
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= self.limit:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


# Using the iterator
for num in SimpleCounter(3):
    print(num)