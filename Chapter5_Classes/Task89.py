#!/usr/bin/python3

'''
We work with the LAB result from the previous lesson.
Add a class-level attribute to the Cake class. Call it known_types.
It will store the sweets produced in our pastry shop.
Assign a list to the variable, for example, in the following form:

['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']

Change __init__ so that if a value that is in the known_kinds
list is passed as the kind parameter, it will be accepted,
but if someone passes a value outside of that list,
other will be written to the newly created object for the kind attribute.
Test the operation of the new __init__ function by creating a "cocoa wafer" object:

cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')

Add a new bakery_offer attribute to the Cake class, which will initially be an empty list.
Change __init__ so that when a new object of type Cake is created,
it is automatically added to the bakery_offer list
Remove from the script the no longer needed instructions
that create the bakery_offer list and add objects of this class to that list.
Change the loop that displays information about the
bakery offer to use the class attribute

Verify that the objects cake01 and others are instances
of class Cake using the isinstance and type functions

Display information about the instance of cake01 and
the class Cake using the vars and dir functions
'''


class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

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
        print('='*30)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')

print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

print('Is cake01 of type Cake? (isinstance)', isinstance(cake01, Cake))
print('Is cake01 of type Cake? (type)', type(cake01) is Cake)
print('vars cake01', vars(cake01))
print('vars Cake?', vars(Cake))
print('dir cake01', dir(cake01))
print('dir Cake?', dir(Cake))