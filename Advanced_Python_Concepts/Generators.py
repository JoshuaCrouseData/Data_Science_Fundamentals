'''
Generators are a simple way to create iterators.
A generator is a function that returns an object (iterator)
which we can iterate over (one value at a time). It is defined
using the 'def' keyword and 'yield' expression.

Create a Generator function that yields numbers, 
starting with 1 and each time incrementing by one 
(similar to the iterator, but as a generator)
'''

def simple_counter(limit):
    num = 1
    while num <= limit:
        yield num
        num += 1

for num in simple_counter(3):
    print(num)