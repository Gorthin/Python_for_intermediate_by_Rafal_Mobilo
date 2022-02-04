#!/usr/bin/python3

import csv

with open('D:\Python\Python_for_intermediate_by_Rafal_Mobilo\Chapter8_Iterators\data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #    for row in csvreader:
    #        print('|'.join(row))
    while True:
        try:
            data = next(csvreader)
            print(data)
        except StopIteration:
            break
    print('All data was processed')