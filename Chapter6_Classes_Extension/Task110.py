#!/usr/bin/env python3

'''
Outside the class, another function has been defined that will
be used in the online baking ordering system. Here it is:

def add_extra_additives(cake, additives):
    cake.add_additives(additives)
The problem is that when placing an order, the customer can select
additives for the baked good. Some of the baked goods already
have these additives, so you can end up with one item among
the ingredients several times. See how the function that adds chocolate and nuts currently behaves:

add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()

add_extra_additives(cake01, ['strawberries', 'sugar-flowers','chocolade', 'nuts'])
cake01.show_info()
You solve this problem by defining a decorator that is also a class,
and then tagging the add_extra_additives function with that decorator

Define the class NoDuplicates

the __init__ method takes a funct argument that stores in local instance variables
the __call__ method has it take the same arguments as
the add_extra_additives function in addition to the self argument. In this method:
define an empty no_duplicate_list, which will only contain
additions that are unique (not already in the additive list in the cake object
go through all the additives to be added to the cake
if such an additive is not yet in the list of additives in the cake, add it to the no_duplicate_list
finally call the funct function passing it the cake object and a new list with unique additives
mark the function add_extra_additives with a decorator pointing to the class NoDuplicates
Test the function. Add-ons that the cake object already had should not be added a second time
'''


class NoDuplicate():
    def __init__(self, funct):
        print(">>> This is init to NoDuplicate")
        self.funct = funct

    def __call__(self, cake, additives):
        no_duplicate_list = []
        for a in additives:
            if not a in cake.additives:
                no_duplicate_list.append(a)
        self.funct(cake, no_duplicate_list)


class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def add_additives(self, additives):
        self.additives.extend(additives)

@NoDuplicate
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()

add_extra_additives(cake01, ['strawberries', 'sugar-flowers', 'chocolade', 'nuts'])
cake01.show_info()