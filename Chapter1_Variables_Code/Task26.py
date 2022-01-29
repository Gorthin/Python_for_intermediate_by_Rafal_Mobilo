#!/usr/bin/python3

'''Using the "clever" method of working with for display messages of the form:
The leader of "...project name..." is ...the leader's name...
The leader of "...project name..."  started ...project start date is ...leader's name...

Using the "clever" combination of enumerate and zip - add to the message
additionally the project sequence number starting from 1:
...sequence number... - The leader of "...project name..."
started ...project start date... is ...name of leader...'''

print("Case 1")
projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for p, l in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(p,l))

print("Case 2")
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for p, d, l in zip(projects, dates, leaders):
    print('The leader of "{}" started {} is {}'.format(p,d,l))

print("Case 3")

for i, (p, d, l) in enumerate(zip(projects, dates, leaders)):
    print('{}. The leader of "{}" started {} is {}'.format(i+1,p,d,l))