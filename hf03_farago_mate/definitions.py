import random
import datetime
from symbol import pass_stmt


def get_random_date():
    date1 = datetime.date(2024, 11, 12)
    date2 = datetime.date(2024, 12, 12)
    time_ellapsed = date2 - date1
    random_date = date1 + datetime.timedelta(days=random.randint(0, time_ellapsed.days))
    return random_date

def get_weather_type():
    weather_types = ["szeles", "napos", "esős", "ködös", "semillen"]
    return random.choice(weather_types)

def get_temperature():
    return str(random.randint(0,20)) + "C"

def get_rain_chance():
    return str(random.randint(0,100)) + "%"

def create_random_weather():
    date = "Datum: " + str(get_random_date())
    weather_type = "Idojaras: " + get_weather_type()
    temperature = "Homerseklet: " + get_temperature()
    rain_chance = "Varhato eso: " + get_rain_chance()
    return [date, weather_type, temperature, rain_chance]

def write_to_txt(number_of_days):
    with open("weather.txt", "w") as text_file:
        for day in range(number_of_days):
            random_weather = create_random_weather()
            for item in random_weather:
                text_file.writelines(item + "\n")

def read_from_txt():
    weathers = {}
    with open("weather.txt", "r") as text_file:
        text = text_file.readlines()
        for line in text:
            line_split = line.strip("\n").split(": ")
            if line_split[0] == "Datum":
                weather = {}
                date = line_split[1]
            if line_split[0] == "Idojaras":
                weather["Idojaras"] = line_split[1]
            if line_split[0] == "Homerseklet":
                weather["Homerseklet"] = line_split[1]
            if line_split[0] == "Varhato eso":
                weather["Varhato eso"] = line_split[1]
            weathers[date] = weather
    return weathers

def get_average_temperature(temperature_list):
    return round(sum(temperature_list) / len(temperature_list), 2)

def get_max_temperature(temperature_list):
    return max(temperature_list)

def is_rainy_day(dict, day):
    if dict[day]["Idojaras"] == "esős":
        return True

def is_semillen_day(dict, day):
    if dict[day]["Idojaras"] == "semillen":
        return True

def get_daily_weather(dict, day):
    print(f'Idojaras a kivalasztott napon ({day}):\n  Idojaras: {dict[day]["Idojaras"]}\n  Homerseklet: {dict[day]["Homerseklet"]}\n  Varhato eso: {dict[day]["Varhato eso"]}')

def get_monthly_weather(dict):
    for day in dict.keys():
        print(f'{day}: {dict[day]["Idojaras"]}, {dict[day]["Homerseklet"]}, varhato eso: {dict[day]["Varhato eso"]}')

def get_statistics(dict):
    try:
        date1 = input("Datumtol (YYYY-MM-DD): ")
        date1_date = datetime.datetime.strptime(date1, "%Y-%m-%d")
        date2 = input("Datumig (YYYY-MM-DD): ")
        date2_date = datetime.datetime.strptime(date2, "%Y-%m-%d")
        temperature_list = []
        rainy_days = 0
        semillen_days = 0
        for day in dict.keys():
            if date1_date <= datetime.datetime.strptime(day, "%Y-%m-%d") <= date2_date:
                temperature_list.append(int(dict[day]["Homerseklet"].strip("C")))
                if is_rainy_day(dict, day):
                    rainy_days += 1
                if is_semillen_day(dict, day):
                    semillen_days += 1
        print(f'Statisztika {date1} es {date2} kozott')
        print(f'  Atlag homerseklet: {get_average_temperature(temperature_list)}C')
        print(f'  Max homerseklet: {get_max_temperature(temperature_list)}')
        print(f'  Esos napok szama: {rainy_days}')
        print(f'  Semillen napok szama: {semillen_days}')
    except ValueError:
        print(f'Helytelen datum...')

def user_menu_choice():
    return input("MENU:\n1. Napi/Havi jelentes lekerese\n2. Ket idopont kozotti statisztika lekerese\n3. Kilepes (end/q/quit)\nValaszd ki a menupontot: ")

def user_daily_monthly():
    return input("Napra vagy honapra keresel? ")

def menu(weather_dict):
    exit = ["quit", "q", "end"]
    menu_choice = user_menu_choice()
    while menu_choice not in exit:

        if menu_choice == "1":
            dm_choice = user_daily_monthly()
            if dm_choice == "nap":
                # print(f'Valaszthato napok: {weather_dict.keys()}')
                user_day_choice = input("Add meg a datumot: ")
                print(weather_dict[user_day_choice])
                get_daily_weather(weather_dict, user_day_choice)
            elif dm_choice == "honap":
                get_monthly_weather(weather_dict)
            else:
                print(f'Rossz erteket adtal meg: {dm_choice}')
        elif menu_choice == "2":
            get_statistics(weather_dict)
        else:
            print(f'Rossz erteket adtal meg: {menu_choice}')
        user_repeat = input("Szeretnel uj statisztikat lehivni (y,n)?  ")
        if user_repeat == "y":
            menu_choice = user_menu_choice()
        else:
            break