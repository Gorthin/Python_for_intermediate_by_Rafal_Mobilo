#!/usr/bin/env python3

'''
A cake shop will specialize in making cakes for various occasions.
Since the Cake class does not have as many specific attributes
to describe new cakes, you decide to create a new class SpecialCake that inherits from the Cake class
The new class has to additionally accept and store the following attributes:
occasion - the occasion from which the cake is ordered
shape - shape of the cake, e.g. square, pyramid, hedgehog, standard
ornaments - additional decorations, e.g. flowers, hearts, leaves
text - the text that should be written on the cake
Using inheritance mechanisms add to the show_info method instructions that display specific to the new class
Create two objects of class SpecialCake: birthday and wedding
Display information about both objects using the show_info() method
For each object in the SpecialCake.bakery_offer list
display the full name property full_name
call the show_info() method
In this task, you should be able to see that you have
everything available in the child class that is in the parent class.
In addition, some functionality can be redefined in your own way.
'''


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

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


class SpecialCake(Cake):
    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments,text):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text

    def show_info(self):
        super().show_info()
        print("Occasion:        {}".format(self.occasion))
        print("Shape:       {}".format(self.shape))
        print("Ornaments:       {}".format(self.ornaments))
        print("Text:       {}".format(self.text))


birthday = SpecialCake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream',
                       'birthday', 'standard', 'hearts', '15')
wedding = SpecialCake('Vanilla Cake', 'cake', 'vanilla', ['whipped cream', 'coconut shirms'], 'strawberries cream',
                      'wedding', 'pyramid', 'pigeons', 'Patricia & Tom')

birthday.show_info()
wedding.show_info()

for cake in SpecialCake.bakery_offer:
    print(cake.full_name)
    cake.show_info()