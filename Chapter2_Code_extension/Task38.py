#!/usr/bin/python3
import math

'''In this assignment you will create a small calculator. The user will enter the formula of a function such as:
2*x
math.sin(x)
3*x**2+2*x-4
and the program will determine the values of this function for x in the interval (0,10) with an accuracy of 0.1
1. import the math module
2. create an empty argument_list
Write a loop that adds the following values to the argument_list
100 values
starting from zero
where each successive one is 0.1 greater than the previous one
4. ask the user to enter a formula. Store the formula in the formula variable.
The user should use the x variable to denote the argument to the function

For each element x in the argument_list, compute the value of the function entered
by the user and display the result'''

argument_list = []
for i in range(101):
    argument_list.append(i/10)
print(argument_list)
print(len(argument_list))
print('')
formula = input("Enter the function formula e.g. 2*x, math.sin(x), 3*x**2+2*x-4 \n")

for x in argument_list:
    result = eval(formula)
    print('Argument x is {0:3.1f}'.format(x))
    print('Result formula is {:6.2f}'.format(result))
    # print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))