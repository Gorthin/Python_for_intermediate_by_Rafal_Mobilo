#!/usr/bin/python3

'''You are building a module that generates graphs. You want to independently influence which colors will be used in the graph. You define a list of colors at the beginning:

["red", "orange", "green", "violet", "blue", "yellow"].

Sometimes the chart will only show 3 categories and then you want to use only the first 3 colors, other times the chart will have 5 categories and you need a list of 5 colors.

Write a function that takes two arguments: a list of colors and the number n. The function is to return a new copy of the color list of length n using the passed argument list.


Write a loop that generates all possible sets of colors available in the list. The loop should handle displaying all sets, even if another color is added to the initial list at some point (don't use typing in a fixed numeric value).

The caption can also be "sliced". Cut from the following text coming from https://nonsa.pl/wiki/Korporacja (formerly nonsensopedia.pl) a fragment explaining the origin of the word "Corporation" - the fragment is in brackets (omit the brackets themselves):

Corporation (from Latin corpo - body, ratus - rat; Polish: body of a rat) -
an organization that under the guise of doing business rules the world today.
It may seem to be a utopian place for realizing professional passions.
In reality, however, it is not so colorful. The corporation is used to exploit
people in the name of progress. It is ruled by the law of the jungle.'''


def get_list_of_colors(colors, n):
    return colors[:n]


colors = ["red", "orange", "green", "violet", "blue", "yellow"]

for i in range(1, len(colors) + 1):
    print(get_list_of_colors(colors, i))

definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '

print(definition[definition.index('(') + 1:definition.index(')')])