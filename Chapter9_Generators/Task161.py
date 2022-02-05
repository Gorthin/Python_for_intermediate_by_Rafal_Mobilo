#!/usr/bin/env python3

'''
Imagine you are an artist looking for inspiration....
You want to compose a hit song, but you have no idea what kind....

You have 7 notes at your disposal:

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
The main theme is supposed to consist of 4 notes. Display all possible arrangements consisting of 4 notes.
I will hint that as far as I know about music, the order of the notes matters.
Use the appropriate function from the itertools module

Using the formula described here:

https://pl.wikipedia.org/wiki/Wariacja_bez_powt%C3%B3rze%C5%84

count how many such potential hit candidates there are.
Note: the function that counts the power is in the math module and is called factorial.
The function that counts the power is called pow
Well, our artist auditioned all the possibilities, but nothing caught his eye.
So we change the assumption. The notes can be repeated, and the order still matters.
Let me hint that this is a 4-element variation with repetitions of a set of notes.
'''
import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for combination in it.permutations(notes, 4):
    print(combination)

print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(
    math.factorial(len(notes))/math.factorial(len(notes) - 4)))

print('='*30)
for combination in it.combinations_with_replacement(notes, 4):
    print(combination)

print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(
        pow(len(notes), 4)))