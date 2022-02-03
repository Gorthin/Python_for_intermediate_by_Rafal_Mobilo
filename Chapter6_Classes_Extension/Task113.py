#!/usr/bin/env python3

'''
add a method that allows you to conveniently format
Cake class objects to text. Let it return a text
consisting of the attributes kind, name and additives
add a method that allows adding a caption to the class.
This caption is to be appended as the next element in the list of additives
modify the above method so that it is possible to pass
more additives at once. All of them are to be appended to the additives list.
modify the above method so that if it is used
to add variables of other types, an error will be generated.
test the above methods
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

    def __str__(self):
        return "Name: {}, Kind: {}, Additives: {}".format(self.name, self.kind, self.additives)

    def __iadd__(self, other):
        if type(other) is str:
            self.additives.append(other)
            return self
        elif type(other) is list:
            self.additives.extend(other)
            return self
        else:
            raise Exception('Sorry - operation not implemented')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake01 += 'cherry'
print(cake01)

cake01 += ['whipped cream', 'raspberry']
print(cake01)

# this will end with an error
# cake01 += 3
# print(cake01)