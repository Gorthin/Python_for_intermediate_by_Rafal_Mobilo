#!/usr/bin/python3

print("Case 1")
'''
In this task we will check how variables behave when their values are modified
In the first case, initialize the variables a, b, c with the value 10. To do so, execute only
one statement.
Display the values of the variables and their identifiers
Then change value of variable a for example to 20
Display values and identifiers of variables again
(identifier of variable a should change
'''

a = b = c = 10
print("a=", a, "b=", b, "c=", c)
print(id(a), id(b), id(c))

a = 20
print("a=", a, "b=", b, "c=", c)
print(id(a), id(b), id(c))

print("Case 2")
'''
Now follow the same steps again as before but with a slight difference:
-variables a, b and c are to be assigned a value in the form of a list, e.g. [1,2,3]
-modification of the variable a should consist in adding a new element to the list a, e.g. the number 4
(the identifier of variable a should now be the same as b and c, in addition the list in variables b and c will also change
'''

a = b = c = [1, 2, 3]
print("a=", a, "b=", b, "c=", c)
print(id(a), id(b), id(c))

a.append(4)
print("a=", a, "b=", b, "c=", c)
print(id(a), id(b), id(c))

'''
Why did this happen?
In the first example, a, b, c were pointers to the memory cell that held the number, the final value
In the second example, a, b, c are pointers to a memory cell that holds a list. The list is a pointer to the elements of that list. When you add a new element to the list, you are not modifying the underlying memory cell with the list, so the id has not changed
'''

print("Case 3")
'''
Note - here you can expect to get different results in different versions of Python, but....
Assign the value 10 to the x variable
Assign the value 10 to the variable y (use assignments on two separate lines!)
Display the id of these variables
(although we're dealing with two independent variables, the python optimizer gave them the same id)
'''
print("Case 3.1")
x = 10
y = 10
print("x=", x, "y=", y)
print(id(x), id(y))

print("Case 3.2")
y = 10 + 1 - 1
print("x=", x, "y=", y)
print(id(x), id(y))

print("Case 3.3")
x = 10
y = 10 + 1234567890 - 1234567890
print("x=", x, "y=", y)
print(id(x), id(y))