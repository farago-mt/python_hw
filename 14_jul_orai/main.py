"""
1. feladat
"""
import random
import math
import datetime
import statistics
import calendar


def today():
    today_date= datetime.date.today()
    day_of_week = calendar.day_name[today_date.weekday()]
    first_day_of_this_year = datetime.date(today_date.year, 1, 1)
    difference_of_dates = today_date - first_day_of_this_year
    difference_of_dates_in_days = difference_of_dates.days
    return f'Today is {day_of_week}, {difference_of_dates_in_days}. day of {today_date.year}'

def generate_random_numbers(count, lowest_number, highest_number):
    return [random.randint(lowest_number, highest_number) for _ in range(count)]

def get_lucky_number(random_numbers):
    return random.choice(random_numbers)

def calculate_avg_sd_min_max_rootofsum(random_numbers):
    average = statistics.mean(random_numbers)
    standard_deviation = statistics.stdev(random_numbers)
    minimum = min(random_numbers)
    maximum = max(random_numbers)
    root_of_sum = round(math.sqrt(sum(random_numbers)), 2)
    return f'Random numbers:\n Average: {average}\n Standard deviation: {standard_deviation}\n Minimum: {minimum}\n Maximum: {maximum}\n Root: {root_of_sum}'

def is_lucky_number_prime(lucky_number):
   pass

def luck_generator():
    print(today())

    random_numbers = generate_random_numbers(10, 1, 100)
    random_numbers.sort()
    print(random_numbers)
    lucky_number = get_lucky_number(random_numbers)
    print(lucky_number)
    print(calculate_avg_sd_min_max_rootofsum(random_numbers))

luck_generator()


"""
2. feladat
"""
def get_birthday():
    birthday = input("Please enter your birthday (month, day): ")
    return birthday


"""
3. feladat
"""

"""
4. feladat
"""
