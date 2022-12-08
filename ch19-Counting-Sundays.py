# https://github.com/splashoui/

# https://projecteuler.net/problem=19

# time module for calculating execution time
import time

# time at the start of program execution
start = time.time()

dictionary_month_day = {1: 31, 3: 31, 4: 30, 5: 31,
                        6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# 7th January 1901 | First Monday after start range.
day, month, year = 7, 1, 1901


list_mondays = []

while year < 2001:

    # Months except Febuary and December
    if month != 2 and month != 12:
        day_limit = dictionary_month_day[month]

        if day + 7 > day_limit:
            day = (day + 7) - day_limit
            month = month + 1
        else:
            day = day + 7

    # February years with 29 days
    elif (month == 2) & (year % 4 == 0):

        day_limit = 29

        if day + 7 > day_limit:
            day = (day + 7) - day_limit
            month = month + 1
        else:
            day = day + 7

    # February each 4 year: 28 days
    elif (month == 2) & (year % 4 != 0):

        day_limit = 28

        if day + 7 > day_limit:
            day = (day + 7) - day_limit
            month = month + 1
        else:
            day = day + 7

    # December conditions to increase the year
    elif month == 12:
        day_limit = dictionary_month_day[month]

        if day + 7 > day_limit:
            day = (day + 7) - day_limit
            month = 1
            year = year + 1
        else:
            day = day + 7

    # Get only the mondays which are the first day of the months and not divisible by 400.
    if (day == 1) and (year % 400 != 0) and (year != 2001):
        list_mondays.append(str(month)+'/' + str(day)+'/'+str(year))

print(f'Answer is {len(list_mondays)}')

# time at the end of program execution
end = time.time()

# total time for program execution
print(f"Execution time: {end - start} ")

# Execution time: 0.0028076171875
