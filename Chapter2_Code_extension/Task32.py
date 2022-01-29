#!/usr/bin/python3

'''At the deposit machine scam from the previous task,
you and your boss decide to open an airline called
"Flying Python". The airline will be domestic. Here is a list of airports:

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
1. build a list of tuples symbolizing the start and end ports. Make a one-to-one connection
2. eliminate the connection from the above list from the port to the same port
Since the connection from A to B is duplicated with the connection from B to A
 - generate possible domestic connections omitting such duplicated routes.
Count the number of generated connections in steps 1,2,3'''

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = [(start, stop) for start in ports for stop in ports]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start != stop]
print(routes)
print(len(routes))

routes = [(start, stop) for start in ports for stop in ports if start < stop]
print(routes)
print(len(routes))