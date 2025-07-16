import datetime
import random

def feladat_1(date, day):
    date_split = date.split("-")
    date_formatted = datetime.date(year=int(date_split[0]), month=int(date_split[1]), day = int(date_split[2]))
    return date_formatted + datetime.timedelta(days=day)

def feladat_2(start, end):
    """ random number generator """
    return random.randint(start, end)

def feladat_3(year):
    """ random date generator in 2024 """
    month = random.randint(1, 12)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month == 2:
        day = random.randint(1, 28)
    else:
        day = random.randint(1, 30)
    return datetime.date(year=year, month=month, day=day)

def feladat_4(list):
    return random.choice(list)

def feladat_5(date1, date2):
    date1_split = date1.split("-")
    date1_formatted = datetime.date(year=int(date1_split[0]), month=int(date1_split[1]), day=int(date1_split[2]))
    date2_split = date2.split("-")
    date2_formatted = datetime.date(year=int(date2_split[0]), month=int(date2_split[1]), day=int(date2_split[2]))
    delta = date1_formatted - date2_formatted
    return delta.days

def feladat_6(a, b, count):
    return random.sample(range(a, b), count)

def feladat_7():
    """ Check if a date is valid """
    pass

def feladat_8(list):
    random.shuffle(list)
    return list

def feladat_9(day, hour, minute):
    return datetime.datetime.now() + datetime.timedelta(days=day, hours=hour, minutes=minute)

def feladat_10(birthday):
    current_date = datetime.date.today()
    current_date_string = current_date.strftime("%Y-%m-%d")
    return feladat_5(birthday, current_date_string)

def feladat_11():
    """rondom number between 1.0 10.0"""
    pass

def feladat_12(a, b):
    return random.choice(feladat_6(a, b, 1))

def feladat_13(list):
    random.shuffle(list)
    return list

def feladat_14():
    current_date = datetime.date.today()
    current_date_string = current_date.strftime("%Y-%m-%d")
    return current_date_string

def feladat_15(list, count):
    random_list = []
    i = 0
    while i < count:
        random_number = random.choice(list)
        if random_number not in random_list:
            random_list.append(random_number)
            i = i + 1
    return random_list


def main():
    print(feladat_1("2025-07-15", 1))
    print(feladat_2(1,100))
    print(feladat_3(2024))
    print(feladat_4(["Alice", "Bob", "Charlie", "Diana"]))
    print(feladat_5("2025-07-18","2025-07-15"))
    print(feladat_6(1, 100, 10))
    # print(feladat_7())
    print(feladat_8(["apple", "banana", "cherry", "date"]))
    print(feladat_9(3, 4, 30))
    print(feladat_10("2025-07-30"))
    # print(feladat_11())
    print(feladat_12(50, 100))
    print(feladat_13([1, 2, 3, 4, 5]))
    print(feladat_14())
    print(feladat_15([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))


main()