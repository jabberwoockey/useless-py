#! /usr/bin/env python3

# https://repl.it/@freeCodeCamp/fcc-time-calculator

def add_time(start, duration, weekday=''):
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday',
                'friday', 'saturday', 'sunday']
    start_hour, start_min = start.split(' ')[0].split(':')

    if start.split(' ')[1] == 'PM':
        start_time = int(start_hour) * 60 + int(start_min) + 720
    else:
        start_time = int(start_hour) * 60 + int(start_min)

    dur_hour, dur_min = duration.split(':')
    end_time = start_time + int(dur_hour) * 60 + int(dur_min)
    end_hour = end_time // 60
    end_min = f'{end_time % 60:>02}'
    end_day = end_hour // 24

    if end_hour % 24 <= 11:
        half = 'AM'
    else:
        half = 'PM'
        end_hour -= 12
    
    if end_hour % 12 == 0:
        end_hour = 12

    if weekday != '':
        end_wday = (weekdays.index(weekday.lower()) + end_day % 7) % 7
        weekday = ', ' + weekdays[end_wday].title()

    if end_day == 0:
        new_time = f'{end_hour}:{end_min} {half}{weekday}'
    elif end_day == 1:
        end_hour -= 24
        new_time = f'{end_hour}:{end_min} {half}{weekday} (next day)'
    else:
        end_hour %= 24
        new_time = f'{end_hour}:{end_min} {half}{weekday} ({end_day} days later)'

    return new_time

print(add_time("3:00 PM", "3:10"))              # Returns: 6:10 PM
print(add_time("11:30 AM", "2:32", "Monday"))   # Returns: 2:02 PM, Monday
print(add_time("11:43 AM", "00:20"))            # Returns: 12:03 PM
print(add_time("10:10 PM", "3:30"))             # Returns: 1:40 AM (next day)
print(add_time("11:43 PM", "24:20", "tueSday")) # Returns: 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12"))            # Returns: 7:42 AM (9 days later)
print(add_time("6:30 PM", "356:11", "friday"))
print(add_time("11:55 AM", "3:12"))             # "3:07 PM"
print(add_time("9:15 PM", "5:30"))              # "2:45 AM (next day)"
print(add_time("11:40 AM", "0:25"))             # "12:05 PM"
print(add_time("2:59 AM", "24:00"))             # "2:59 AM (next day)"
print(add_time("8:16 PM", "466:02"))            # "6:18 AM (20 days later)"
print(add_time("5:01 AM", "0:00"))              # "5:01 AM"
print(add_time("8:16 PM", "466:02", "tuesday")) # "6:18 AM, Monday (20 days later)"
print(add_time("11:59 PM", "24:05", "Wednesday")# "12:04 AM, Friday (2 days later)"
print(add_time("2:59 AM", "24:00", "saturDay")  # "2:59 AM, Sunday (next day)"
