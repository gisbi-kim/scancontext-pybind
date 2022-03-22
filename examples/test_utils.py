import os 
import sys 
import time 
from functools import wraps

#
curr_dir = os.path.dirname(__file__)

#
time_verbose = True 

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        if time_verbose:    
            print(f' function {func.__name__}: {total_time*1000:.3f} ms')
        return result
    return timeit_wrapper

def timeit_sec(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        if time_verbose:    
            print(f' function {func.__name__}: {total_time:.1f} s')
        return result
    return timeit_wrapper
