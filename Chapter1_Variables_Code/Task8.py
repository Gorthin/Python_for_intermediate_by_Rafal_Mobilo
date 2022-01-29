#!/usr/bin/python3

'''Here is the declaration of the days variable:
days = ['mon','tue','wed','thu','fri','sat','sun']
create a workdays variable that will initially contain the same elements as days
then remove days off from workdays
finally, display the days and workdays and make sure that saturday and sunday only disappear from the workdays list'''

days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')

print("Days: ", days, id(days))
print("Workdays: ", workdays, id(workdays))