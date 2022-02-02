#!/usr/bin/python3

'''
In this assignment, we continue to work on the class "Cake"
Add a hidden gluten_free attribute to the Cake class.
(This is one of the most important pieces of information
about baked goods, so we try to make sure that this attribute
can only be set once when we create the object, so that
later when the program is running we don't accidentally change the value in this field)
Change the __init__ and show_info functions to support the new class attribute
When creating new baked goods objects pass True or
False value indicating if the baked good is gluten free
(as far as I know eggs do not contain gluten so meringues are gluten free)
Test the program
Try to change __gluten_free attribute in the program code
(e.g. after displaying cake shop offer)
Do you get an error after running? Why. Use dir(cake03)
command to see what attributes this object has
Change the attribute value using a specially and
automatically created attribute with a specific structure as it was done in the video
Display the information about cake03 (meringue) again - has it now become a gluten product?
'''


class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free):
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
        print("Gluten : {}".format(self.__gluten_free))
        print('='*30)


    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', True)
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False)
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '',True)
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa',False)

print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

print('Is cake01 of type Cake? (isinstance)', isinstance(cake01, Cake))
print('Is cake01 of type Cake? (type)', type(cake01) is Cake)
print('vars cake01', vars(cake01))
print('vars Cake?', vars(Cake))
print('dir cake01', dir(cake01))
print('dir Cake?', dir(Cake))


cake03.__gluten_free = False
print(dir(cake03))
cake03._Cake__gluten_free = False
cake03.show_info()