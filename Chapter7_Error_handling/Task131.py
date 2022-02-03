#!/usr/bin/env python3

'''
Your task is to write a class method named publish_offer that:
takes a list of tours as an argument
declares a local list_of_errors, which stores the test results for tours containing errors
calls the check_data method for each tour in the list of errors
if the error is a ValueError, add a message like "<trip symbol>: <error content>" to the list_of_errors
if the error is an Exception, it will add to the list_of_errors a string of the form "<trip symbol>: <trip content>"
if after checking all trips in list_of_errors there are any errors,
it will report an exception with the text "The list of trips has errors: <list_errors>"
otherwise it will display the message "the offer will be published..."
(normally this is where the publishing of trips would take place, but we'll skip this point)
In the code outside the class, add a call to the publish_offer method such that:
in the try block:
first the message about the start of the tour check will be displayed
then the publish_offer method is called
at the end "done" will be displayed
in the except block:
if an error has occurred, display a "scary" error message and details of that error
'''

import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")

    @classmethod
    def publish_offer(cls, trips):
        list_of_errors = []

        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))

        if len(list_of_errors) > 0:
            raise Exception("The list of trips has errors: {}".format(list_of_errors))
        else:
            print('The offer will be published...')


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('... done')
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')