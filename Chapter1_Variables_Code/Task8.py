#!/usr/bin/python3

days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')

print("Days: ", days, id(days))
print("Workdays: ", workdays, id(workdays))