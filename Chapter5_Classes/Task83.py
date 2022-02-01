#!/usr/bin/python3

'''
The boss of the pastry shop where you work has
asked you to write a program that necessarily has to be object-oriented!

We start by defining the Cake class, which should have attributes:
-name describing the name of the product
-kind describing the type of baked goods e.g. cakes, cookies, muffins, meringues
-taste containing the main flavor
-additives - containing a list of additives for the given cake, e.g. fruit, sprinkles, toppings etc., if the cake has no additives, it will be an empty list
-filling - description of the filling, if the given cake has no filling it will be an empty list
-... you can add further ideas of your own :)
After defining the class, create a few instances of
this class, it's a good moment to enrich the vocabulary
of sweetness in English, but if you prefer - you can do it in Polish
Create a list bakery_offer and add to it instances
of previously created objects of class Cake
Write a loop going through all the instances of the
class in the bakery_offer list and display something like
(the data coming from the instances has been bolded):

Today in our offering:
Vanilla Cake - (cake) main flavor: vanilla with additives of ['chocolade', 'nuts'], filled with cream
Chocolade Muffin - (muffin) main taste: chocolade with additives of ['chocolade'], filled with
Super Sweet Maringue - (meringue) main taste: very sweet with additives of [], filled with
'''

class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')

bakery_offer = []
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)

print("Today in our offer:")
for c in bakery_offer:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(
        c.name, c.kind, c.taste, c.additives, c.filling))