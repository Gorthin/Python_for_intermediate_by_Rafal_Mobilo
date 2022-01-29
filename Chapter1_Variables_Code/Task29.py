#!/usr/bin/python3

'''You are writing a program that will support a deposit machine.
This will be a state-of-the-art deposit machine that
you can also deposit coins into. Whenever someone deposits
money you have to count how many bills or coins of
a given denomination are in the cashier.

Using any method, create a dictionary which will store
the value of the denomination as a key, and as far as
the dictionary values are concerned, they are supposed
to be zero for now. I suggest calling this dictionary dict_denominations.

Write a for command that will display how much money
we have in certain coins or bills. The list should
start with the smallest denominations and end with the largest.
If you like, make sure to format the result nicely:
-denomination in 6 characters, including 2 decimals
-number of coins/banknotes - integer, max. 5 digits'''

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
dict_denominations = {}

for d in banknotes_coins:
    dict_denominations[d] = 0

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

dict_denominations[500] += 1

for key in sorted(dict_denominations):
    print('Denominate: {0:6.2f} - amount {1:5}'.format(key, dict_denominations[key]))