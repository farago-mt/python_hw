import json
import statistics

"""
1. feladat
"""
print("1. feladat")
json_dict = {"nev": "Anna", "kor": 25, "varos": "Budapest"}
with open("1_feladat.json", "w") as file:
    json.dump(json_dict, file)
with open("1_feladat.json", "r") as file:
    print(file.read())

"""
2. feladat
"""
print("2. feladat")
with open("felhasznalok.json", "r", encoding="utf-8") as file:
    json_2 = json.load(file)
print(json_2)
for element in json_2:
    element["orszag"] = "Magyarorszag"
with open("felhasznalok_updated.json", "w", encoding="utf-8") as file:
    json.dump(json_2, file)


"""
3. feladat
"""
print("3. feladat")
with open("szamok.json", "r", encoding="utf-8") as file:
    json_3 = json.load(file)
print(json_3)
json_3.sort()
with open("szamok_sorted.json", "w", encoding="utf-8") as file:
    json.dump(json_3, file)

"""
4-5.feladat
"""
with open("pontszamok.json", "r", encoding="utf-8") as file:
    json_4_5 = json.load(file)
print("4-5.feladat")
print(json_4_5)
print(f'min: {min(json_4_5)}')
print(f'max: {max(json_4_5)}')
print(f'sum: {sum(json_4_5)}')
print(f'mean: {sum(json_4_5)/len(json_4_5)}')

"""
6. feladat
"""
print("6. feladat")
def check_json(json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            json_6 = json.load(file)
    except FileNotFoundError as e:
        print(e)
        default_json = {"uzenet": "Ez egy alapértelmezett JSON fájl."}
        with open("default.json", "w", encoding="utf-8") as file:
            json.dump(default_json, file)

check_json("pontszamokk.json")


"""
7.feladat
"""
print("7.feladat")
# try:
#     with open("hibas_json.json", "r", encoding="utf-8") as file:
#         json_6 = json.load(file)
#         print(json_6)
def is_valid_json(json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            json_7 = json.load(file)
            print("valid json")
    except:
        print("invalid json")

is_valid_json("pontszamok.json")
is_valid_json("hibas_json.json")

"""
8.feladat
"""
print("8.feladat")
with open("felhasznalok.json", "r", encoding="utf-8") as file:
    json_8 = json.load(file)
for element in json_8:
    if element["kor"] >30:
        print(element)

"""
9. feladat
"""
print("9. feladat")
with open("szavak_50.txt", "r", encoding="utf-8") as file:
    szavak_list = file.read().split("\n")
    print(szavak_list)
with open("szavak_json.json", "w", encoding="utf-8") as file:
    json.dump(szavak_list, file)

"""
10. feladat
"""
print("10. feladat")

"""
11. feladat
"""
print("11. feladat")
with open("dolgozok.json", "r", encoding="utf-8") as file:
    json_11 = json.load(file)
print(json_11)

fizetes = []
for element in json_11:
    fizetes.append(element.get("fizetés"))
print(fizetes)
for element in json_11:
    if element.get("fizetés") == min(fizetes):
        print(f'min fizetes: {element.get("név")}')
    if element.get("fizetés") == max(fizetes):
        print(f'max fizetes: {element.get("név")}')