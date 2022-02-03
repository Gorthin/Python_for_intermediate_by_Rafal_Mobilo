#!/usr/bin/env python3

'''
You need to define a NoDuplicates class that will have only one attribute, list.
This attribute is a list, which is supposed to store only unique values.
Define the NoDuplicates class
In the __init__ method, create an attribute of the list class that will be an empty list
Add the __call__ method
method should take self argument and list with new objects to be stored in new_items list
for each item in new_items, if that item is not already in the list, add it to the list
Test the class
Create a my_no_dup_list object that will be an instance of the NoDuplicates class.
Display this object.
By calling the instance, add the items in the ['keyboard','mouse']
list to the list. Display this object. Both subtitles should be added to the list
By calling the instance, add the items in the list
['keyboard','mouse','flash drive'] to the list.
Display this object.  Only the flash drive should be added
Calling the instance add the items from the list
['charger','pendrive'] to the list.Display this object.
Only the charger should be added
'''


class NoDuplicates(list):
    def __init__(self):
        self.list = []

    def __call__(self, new_items):
        for a in new_items:
            if not a in self.list:
                self.list.append(a)


my_no_dup_list = NoDuplicates()
print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'mouse'])
print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
print(my_no_dup_list.list)

my_no_dup_list(['charger', 'pendrive'])
print(my_no_dup_list.list)