'''
Decorators are a powerful and expressive feature in Python, 
allowing you to alter the behavior of a function or method.
They are especially useful for logging, performance tasks, 
transaction processing, caching, and authorization.

Create a decorator that logs the execution time of a function.
'''

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Executing {func.__name__} took {end_time - start_time} seconds.")
        return result
    return wrapper


# Applying the decorator
@timing_decorator
def sample_function(delay):
    """Function to add delay"""
    time.sleep()
    return "Done"

print(sample_function(1))