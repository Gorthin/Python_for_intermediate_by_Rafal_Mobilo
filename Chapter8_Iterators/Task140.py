#!/usr/bin/python3

'''
Your company will be performing a sales analysis for a customer. One of the algorithms states that:
for each product (and there are 500 of them)
simulate each type of promotion (and there are 50 of them)
and predict the sales results for a sample of customers (and there are 500 of them).
Since you will be performing analyses on even larger data sets, your task is to rewrite the above code into an iterator.
Define the Combinations class
In the __init__ method
method, take the products, promotions, customers parameters and store them as class attributes.
Also define three attributes: current_product, current_promotion, current_customer and assign them the value 0.
When returning a product-promotion-customer combination, these numbers will point to the currently returned
item from the products, promotions, customers lists

Define a __next__ method that:
Checks if current_customer is >= from the length of the customers list.
If so, set current_customer to 0 and increase current_promotion by 1
Checks if current_promotion is >= from the length of the promotions list.
If so, set the value of current_promotion to 0, and increase the value of current_product by 1
Check if current_product is >-= from the length of the products list.
If so, set the value of current_product to -0 and report a StopIteration exception
write to the local variable item_to_return the combination formed as an item
from the products list pointed to by the number current_product, an item from the promotions list
pointed to by the number current_promotion and an item from the customers list pointed to
by the number current_customer
increments current_customer by 1
return the item_to_return variable
Define the __iter__ method that returns the self object
Remove this fragment of the original script

combinations = []

for i in products:
    for j in promotions:
        for k in customers:
            combinations.append("{} - {} - {}".format(i, j, k))
Instead

Create an instance of the Combinations class and store it in the combinations variable
For each element of combinations variable, execute pass
Run the program and measure the amount of memory used by this program.
'''

import time

'''
Bad solution
products = ["Product {}".format(i) for i in range(1, 500)]
print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 50)]
print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 500)]
print(customers)

combinations = []

for i in products:
    for j in promotions:
        for k in customers:
            combinations.append("{} - {} - {}".format(i, j, k))

for c in combinations:
    # here an analysis will be done - currently, just nothing happens :)
    pass

time.sleep(10)'''

class Combinations:
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0

    def __next__(self):
        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1

        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration()

        item_to_return = "{} - {} -{}".format(self.products[self.current_product],
                                              self.promotions[self.current_promotion],
                                              self.customers[self.current_customer])

        self.current_customer += 1

        return item_to_return

    def __iter__(self):
        return self


products = ["Product {}".format(i) for i in range(1, 500)]
promotions = ["Promotion {}".format(i) for i in range(1, 50)]
customers = ['Customer {}'.format(i) for i in range(1, 500)]

combinations = Combinations(products, promotions, customers)

for c in combinations:
    pass

time.sleep(10)