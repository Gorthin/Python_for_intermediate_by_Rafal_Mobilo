#!/usr/bin/python3

'''
Here is the code of a certain program:

cake_01_taste = 'vanilla'
cake_01_glaze = 'chocolade'
cake_01_text = 'Happy Brithday'
cake_01_weight = 0.7

cake_02_taste = 'tee'
cake_02_glaze = 'lemon'
cake_02_text = 'Happy Python Coding'
cake_02_weight = 1.3


def show_cake_info(taste, glaze, text, weight):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        taste, glaze, text, weight))

show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)


Change it using the following techniques:
change the definition of variables to a dictionary with properties
change the definition of the function so that it takes one parameter
and still displays the information passed in by the parameter
create a list of cakes and pass through the list to display
the information returned by the show_cake_info function
'''

cake1 = {
'taste' : 'Vanilia',
'glaze' : 'chocolade',
'text' : 'Happy Brithday',
'weight' : 0.7
}

cake2 = {
'taste' : 'Tee',
'glaze' : 'lemon',
'text' : 'Happy Python Coding',
'weight' : 1.3
}

def show_cake_info(type_cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        type_cake['taste'], type_cake['glaze'], type_cake['text'], type_cake['weight']))


cakes = [cake1, cake2]

for a_cake in cakes:
    show_cake_info(a_cake)