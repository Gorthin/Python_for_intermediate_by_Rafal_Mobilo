#!/usr/bin/python3

'''Write the following if statement in simplified form.

Write a program that:
-writes in the variable today_weekday the name of today's day of the week
-based on the first verse of the song, use a series of if/elif/.../else statements to determine what you should do today
-Reproduce the above program using the simplified syntax of the if statement'''

import datetime as dt


print("Case 1")

price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)

price = price - bonus if bonus_granted else price
print(price)

print("Case 2")

rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

rating = 'very good' if rating == 5 else 'good' if rating == 4 else 'weak'
print(rating)

print("Case 3")
'''W poniedzialek, w poniedziałek ja nie mogę bo pomagam mamie
A we wtorek, a we wtorek i środę ty masz w domu pranie
No a w czwartek, no a w czwartek ja mam dyżur, w piątek, w piątek dwa zebrania
Ty w sobotę, ty w sobotę znów nie możesz bo na lekcje ganiasz
ALE ZA TO NIEDZIELA ALE ZA TO NIEDZIELA NIEDZIELA BĘDZIE DLA NAS!!!!!!!!!

Monday, Monday I can't because I'm helping my mom
And on Tuesday, and on Tuesday and Wednesday you have laundry at home
And on Thursday, and on Thursday I'm on duty, and on Friday, on Friday two meetings
Saturday, you can't do it again on Saturday because you have to go to class
BUT SUNDAY BUT SUNDAY SUNDAY WILL BE FOR US!!!!!!!!!
'''

today_weekday = dt.date.today().strftime("%A")

if today_weekday == 'Monday':
    print("I'm helping my mum")
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print("You are doing laundry")
elif today_weekday == 'Thursday':
    print("I'm on duty")
elif today_weekday == 'Friday':
    print("I have two meetings")
elif today_weekday == 'Saturday':
    print("You have lessons")
else:
    print("SUNDAY WILL BE FOR US")

print("I'm helping my mum" if today_weekday == 'Monday' else
      "You are doing laundry" if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else
      "I'm on duty" if today_weekday == 'Thursday' else
      "I have two meetings" if today_weekday == 'Friday' else
      "You have lessons" if today_weekday == 'Saturday' else
      "SUNDAY WILL BE FOR US")