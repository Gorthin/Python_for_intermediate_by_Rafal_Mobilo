#!/usr/bin/python3
import math, time
'''In this task, you will repeatedly calculate values calculated
by formulas and then compare execution times depending on how the code is interpreted.
1. import the math and time modules
2 Create a list with formulas:

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
3. prepare an argument list (if the loop takes too long reduce the number of elements in this list):
argument_list = []
for i in range (1000000):
    argument_list.append(i/10)
3. for each formula in the formula list:
Create an empty list results_list = []
Display the formula that the loop is working on now
Store the current time in the start variable
For each argument in the argument_list, calculate the formula value and add it to the results_list
Display the information about the minimum and maximum calculated value in the results list
Store the current time in the stop variable
Display information about the duration of the calculation
Test the script
Copy the loop from step (3) and modify it:
Before the loop counting the formula value, insert an instruction storing the compiled code in the compiled_formula variable
In the loop counting formula value use the precompiled code from the compiled_formula variable
6. run the program and compare the times before and after optimization'''

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range (100000):
    argument_list.append(i/10)

for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    non_compiled_time = stop - start
    print("Calculation non compiled time: {}".format(non_compiled_time))

print('-'*30)
print("Compiled formula:")
for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))

    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    compiled_time = stop - start
    print("Calculation compiled time: {}".format(compiled_time))

difference = non_compiled_time / compiled_time
print("Compiled time is a {0:3.1f} faster then non compiled".format(difference))