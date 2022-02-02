#!/usr/bin/python3

'''
In this LAB we work with the class from the previous lesson
(if you don't have the solution copy my proposed solution from the previous lesson)
We need to add hidden attribute __text to the class.
It is responsible for the caption placed on the cake.
In the __init__ function, take a new argument text

Store it in the __text variable by performing a check:
the caption can only be stored in the instance if kind is 'cake'
or text is an empty caption. If these conditions are not met,
display a diagnostic message (print for you so you know what's going on)

Add an implicit function __get_text that will return the value stored in __text

Add an implicit function __set_text that will take an additional
argument new_text and update the __text attribute only for products with the kind 'cake'

Define a Text property that uses the above functions.

When creating objects of the Cake class, pass an additional
text argument - place empty or other typical 'cake' text,
some valid (i.e. the text on the cake) and some invalid (i.e. the text on the wafer)

Display all information about all baked goods

Try to insert the text on the cake and on the other non-cake baked goods into the Text property - trace the correctness of these operations by displaying the bakery offer again
'''


class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print("The text will only fit on the cake.")


    def show_info(self):
        print("Name: {}".format(self.name).upper())
        print("Taste : {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("- {}".format(a))
        if len(self.filling) > 0:
            print("Filling:")
            print("- {}\n".format(self.filling))
        print("Texr on a cake : {}".format(self.__text))
        print("Gluten : {}".format(self.__gluten_free))
        print('='*30)


    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('Text can be set only for cake ({})'.format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on the cake')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', True, "Happy Birthday!")
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '',True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa',False, "I love Yout")

print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

cake01.Text = 'Happy birthday!'
cake02.Text = '18'

for c in Cake.bakery_offer:
    c.show_info()