#!/usr/bin/python3

'''TASK 1

You are developing a program for a paint store.
Customers sometimes ask how much paint is needed to paint an apartment.
Write a function calculate_paint that:
accepts an argument efficency_ltr_per_m2 - specifying how much paint is needed to paint a square meter
takes any number of successive arguments corresponding to areas to be painted for rooms of the apartment that is to be painted
the function returns information about the amount of paint needed
Test the function in two ways:
by passing the surfaces to be painted in each room simply after the decimal point by calling the function
by defining a list with surfaces and then passing this list to the function

TASK 2
You are writing a function called log_it, which is supposed
to save the arguments sent to the function in a text file,
e.g., c:∆temp_log_it.txt. The function will be used elsewhere
in the program, where it will be called at strategic moments,
documenting how the program works. If you have no other ideas then make sure that:

it is possible to send any number of arguments
when adding information to the file, separate individual arguments with a space
at the end of the file write ENTER, so that the next call of the function writes from the new line
Translated with www.DeepL.com/Translator (free version)'''

print("Case 1")

def calculate_paint(efficency_ltr_per_m2, *args):
    total_area = sum(args)
    paint = total_area * efficency_ltr_per_m2
    return paint


print(calculate_paint(0.5, 37, 45, 90))

rooms = [47, 65, 23]
print(calculate_paint(0.5, *rooms))

print("Case 2")


def log_it(*args):
    path = r'D:\Python\Python_for_intermediate_by_Rafal_Mobilo\Chapter3_Funktion\log_it.txt'
    with open(path, "a") as f:
        for line in args:
            f.write(line)
            f.write(' ')

        f.write("\n")


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')