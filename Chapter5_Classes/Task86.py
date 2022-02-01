#!/usr/bin/python3

'''
Add 3 methods to the class from the previous task:
show info, which
displays the product name in capital letters
display flavor information
if the product has any additives, it will display them
if the product has a filling, it will display it
(of course test the function after implementation)
set_filling, which
takes as argument the name of the pie filling
saves it in the filling attribute for the cake
(of course, test the function after implementation)
add_additives, which
takes as argument a list of additives
adds the values from the list to the current list of additives
(test this function too)
Then add cream filling to the muffin, and coconut
and cocoa sprinkles to the meringue.
Display the baked goods modified this way.
'''

class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

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
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], 'cream')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', ['cocos', 'chocolade'], '')

bakery_offer = []
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)

cake02.set_filling('vanilla cream')
cake03.add_additives(['cocoa powder', 'coconuts'])

print("Today in our offer:")
for c in bakery_offer:
    c.show_info()