#!/usr/bin/python3
import time
import functools


'''
Here is an example of a not very well written function
that calculates the value in a Finobacci string:

def fib(n):

    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)

    return result
Instead of calculating the values from the smallest
to the largest and using the previous results
to determine subsequent values, the function determines
the previous values each time. Optimize the function
using the cache method, (and if you feel like it,
rewrite the function to a better form)
Prepare the function for the timing test
import time module
save the current time in the start variable
write a loop that calculates the value of a string
starting from 1, and ending on a value that makes
sense on your computer, that you have the patience
to wait for (in my case it's about 33-37)
each time display the number of iterations in
the loop and the difference between
the current time and the time from the start variable
save the duration of calculations
optimize the function
import the functools module
mark the fib function with the lru_cache
decorator with the maximum number of stored results 100
at the end of the script add an
instruction that displays the result of the cache_info command
compare the results
'''

@functools.lru_cache(100)
def fib(n):

    time.sleep(0.1)
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)
    return result

start = time.time()

for i in range(34):
    counter = fib(i)
    print('{0:2d}  {1}, time = {2:3.2f}'.format(i, counter, time.time() - start))

stop = time.time()
print("Executed {}".format(stop - start))

print(fib.cache_info())