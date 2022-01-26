#!/usr/bin/python3

'''The script is supposed to:
run until the user selects something and presses enter
after entering the value check if this value is a number
if it is not a number it should display a message about it
if it is a number it has to check if it is one of the allowed option numbers
if it is, it has to display the message with the number of the chosen option and the content
if it is not, it has to display a message that an invalid option has been chosen
'''

def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i + 1, options[i]))

    choice = input('Select option above or press enter to exit: ')
    return choice


choice = 'x'
options = ['load data', 'export data', 'analyze & predict']

while choice:

    choice = DisplayOptions(options)

    # executed only if something was entered
    if choice:
        try:
            choice_num = int(choice) - 1
            if choice_num >= 0 and choice_num < len(options):
                print("you have selected {} - {}".format(choice_num + 1, options[choice_num]))
            else:
                print("Choose a value from a list or press enter")
        except:
            print("You need to enter a number")
    else:
        print('----- END -----')