#!/usr/bin/env python3

import datetime
# import logging

WEEKDAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

timetable = {
    "valid_from": "2018-08-01", 
    "valid_to": "2019-06-19",
    'label': 'Klasse 4c',
    "lessons": 
    { "Mon": ["D", "D", "Sp", "Eng", "Eng", "SK"], # lessons on Monday 
      "Tue": ["D", "D", "SK", "Ma", "Mu", "Sp"],
      "Wed": ["Ma", "Ma", "SK", "", "R", "D", "Eng"],
      "Thu": ["", "Ma", "D", "SK", "Ma", "R", "", "", ""],
      "Fri": ["Ku", "Ku", "Sp", "", "Mittagessen", "SK", "D"],
      "Sat": []
    },
    "start_times": ["8:00", "8:55", "10:00", "10:50", "12:00", "12:50", "13:45"],
    "end_times":   ["8:45", "9:40", "10:45", "11:35", "12:45", "13:35", "14:25"]
    }
    
def get_all_lessons(tt):
    # returns a deduped list of all lessons
    
    lessons = tt['lessons']
    lessons_result = [] # alternatively we could use set() 
    for day in WEEKDAYS:
        lessons_per_day = lessons[day]
        for lesson_item in lessons_per_day:
            if lesson_item and lesson_item not in lessons_result:
                lessons_result.append(lesson_item)
    return lessons_result

def get_days_by_lesson(tt, lesson):
    # returns a deduped list of days this lesson is taught on
    
    lessons = tt['lessons']
    days_result = []
    for day in WEEKDAYS:
        lessons_per_day = lessons[day]
        for lesson_item in lessons_per_day:
            if lesson_item == lesson:
                days_result.append(day)
                break
    return days_result
    
def get_lessons_by_day(tt, day = datetime.date.today()):
     # returns list of lessons on given day
     # expects ISO formatted string as input date e.g. 2018-05-13
    
    lessons = tt['lessons']
    if isinstance(day, str):
        day = datetime.date.fromisoformat(day)
    # print(day)
    weekday = day.isoweekday()
    # print(weekday)
    day_name = WEEKDAYS[weekday-1]
    # print(day_name)
    return lessons[day_name]
    
def get_start(tt, day = datetime.datetime.today()):
     # returns begin of first lesson for given day
     # expects ISO formatted string as input date e.g. 2018-05-13 or else defaults to today
    
    lessons = tt['lessons']
    start_times = tt['start_times']
    if isinstance(day, str):
        day = datetime.date.fromisoformat(day)
    # print(day)
    weekday = day.isoweekday()
    # print(weekday)
    day_name = WEEKDAYS[weekday-1]
    # print(day_name)
    lessons_day = lessons[day_name]
    i = 0
    while i < len(lessons_day):
        if lessons_day[i]:
            break
        i += 1
    return start_times[i]
    
def get_end(tt, day = datetime.datetime.today()):
     # returns end of last lesson for given day
     # expects ISO formatted string as input date e.g. 2018-05-13 or defaults to today
    
    lessons = tt['lessons']
    end_times = tt['end_times']
    if isinstance(day, str):
        day = datetime.date.fromisoformat(day)
    weekday = day.isoweekday()
    day_name = WEEKDAYS[weekday-1]
    lessons_day = lessons[day_name]
    i = len(lessons_day)-1
    while i >= 0:
        # (last) lesson item could be empty string
        if lessons_day[i]:
            break
        i -= 1
    return end_times[i]

lesson = 'D'
day = '2018-12-10'
print(f'An welchen Tagen habe ich {lesson}?')    
print(get_days_by_lesson(timetable, 'D'))
print(f"Welche Faecher gibt es in {timetable['label']}?")
print(get_all_lessons(timetable))
print('Welche Faecher habe ich heute?')
print(get_lessons_by_day(timetable))
print(f'Welche Faecher habe ich am {day}?')
print(get_lessons_by_day(timetable, day))
print('Wann beginnt heute die Schule?')
print(get_start(timetable))

day = '2018-12-14'
print(f'Wann endet die Schule am {day}?')
print(get_end(timetable, day))
print('Wann endet die Schule heute?')
print(get_end(timetable))
