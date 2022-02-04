#!/usr/bin/python3

'''
Our goal is to eliminate the __next__ method and replace it with __getitem__, which will allow us to refer
to the i-th generated element. At the same time, however, we still want to be able to use the object in a
for loop, and you know that by default you need the __next__ method to do that. You get around this
problem by using a trick with the iter() function

But one step at a time:
Remove the definition of the __next__ method
The variables current_product, current_promotion and current_customer initialized in __init__ will also no longer be needed
Add the definition of the __getitem__ method to the class
If item is greater than the number of items the class object can generate, then raise a StopIteration exception
hint - the maximum number of generated combinations is the number of products times the number of promotions times the number of customers
Otherwise, you need to calculate what combination should be returned and for this purpose
in the pos_products variable, write the result of dividing the total value of the item by
the number of promotions times the number of customers
update the item variable with the result of dividing the item value modulo the number of promotions times the number of customers
write in the pos_promotions variable the result of dividing the total value of item by the number of customers
update the item variable with the result of dividing the item value modulo the number of customers
write the item value in the pos_customers variable
now the variables pos_products, pos_promotions and pos_customers indicate the correct items
for the lists products, promotions and customers to be returned
Return a caption consisting of the list item products located at item pos_products and
the list item promotions located at item pos_promotions and the list item customers located at item pos_customers
In the main part of the script write a for loop that:
assign to the control variable i values from 1 to 30 (this is how many possible combinations
we have now - 3 products * 2 promotions * 5 customers)
in each execution of the loop will display the i-th element from the combinations object.
Thanks to the fact that the Combinations class now has a __getitem__ method you will see all
possible combinations of products, promotions and customers
Once you have finished testing, comment out this loop
Check if it is possible to get more items from the combinations object using the next function (it should not be possible)
Do something to make it work! :)
Hint: Remember about the iter() function
Test fetching consecutive elements using next()
Write a for loop that goes through all possible combinations returned by the combinations object, but don't use the control variable!
'''


class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

    def __getitem__(self, item):

        if item >= len(self.products) * len(self.promotions) * len(self.customers):
            raise StopIteration()
        else:
            pos_products = item // (len(self.promotions) * len(self.customers))
            # print(item, (len(self.promotions) * len(self.customers)), pos_products)
            item = item % (len(self.promotions) * len(self.customers))

            pos_promotions = item // len(self.customers)
            item = item % len(self.customers)

            pos_customers = item

            return "{} - {} -{}".format(self.products[pos_products],
                                        self.promotions[pos_promotions],
                                        self.customers[pos_customers])


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)

# for i in range(0, 31):
#    print(i, combinations[i])

combinations_iterator = iter(combinations)
print(next(combinations_iterator))

for c in combinations_iterator:
    print(c)