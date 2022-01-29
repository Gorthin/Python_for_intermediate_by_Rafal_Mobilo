#!/usr/bin/python3


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