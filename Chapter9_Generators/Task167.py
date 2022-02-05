#!/usr/bin/env python3

'''
A perfect number is a natural number that is the sum of all its proper divisors (that is, smaller than it).
Well, let's look for perfect numbers in the range from 1 - 10000. Here's a function that determines the divisors of a number:

def get_factors(x):

    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list
Test the function by determining the divisors of the number 20.
In candidate_list variable write numbers from 1 to 10000 (processing will take some time so you can start with smaller value like 100)
In filtered_list variable write only those numbers from candidate_list, which are perfect
use filterfalse function from itertools module
on each number from candidate_list
check if the sum of the numbers in the list returned by get_factors for this number is different from this number
Convert the result to a list
For each item in the filtered_list, display that number and a list of its divisors (call get_factors again)
And now something that wasn't in the VIDEO lesson: islice
The islice object is created based on a generator.  You know that generators are often like lists,
and in lists you can refer to subsets using slice operations. The idea behind using the islice
operator is that the gerator will only generate numbers when you cut them (the slice operation).
Suppose we are looking for prime numbers up to 10000. To check if a number has divisors we could use:

def check_if_has_dividers(x):

    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False
Assuming you want to display ALL prime numbers up to 10000 you can do it like this:
# not optimal:
prime_numbers = list(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
print(prime_numbers)
Notice that the computer had to count this for a while... If you want to display only the 10 initial values you would do it like this:
print(prime_numbers[:10])
Even though we're only displaying 10 prime numbers, they all had to be calculated first anyway.
And that takes.... and this is where islice comes in:
prime_numbers = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 10)
print(list(prime_numbers))
See that by instantiating this object we are doing this up to 10000000. Despite this we get the results very quickly.
Why? Because islice will finish generating more numbers when it returns 10. Clever! As an exercise,
rewrite/copy this code for yourself and see how it works.
'''

import itertools as it


def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list


print(get_factors(20))

candidate_list = list(range(1, 10001))
filtered_list = list(it.filterfalse(lambda x: x != sum(get_factors(x)), candidate_list))

for p in filtered_list:
    print(p, get_factors(p))