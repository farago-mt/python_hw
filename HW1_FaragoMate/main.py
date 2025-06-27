# 1. feladat
""" Kérj be egy szöveget, és számold meg, hány magánhangzót tartalmaz! """
def count_vowels():
    vowels = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']
    text = input("Írj be egy szöveget: ")
    counter = 0
    for letter in text.lower():
        if letter in vowels:
            counter += 1
    print(f'A {text} {counter} db magánhangzót tartlamaz.')

# count_vowels()

# 2. feladat
""" Kérj be egy egész számot, majd számold össze a számjegyeit! """
def sum_of_digits():
    number = input("Írj be egy számot: ")
    sod = 0
    for digit in number:
        sod += int(digit)
    print(f'A {number} számjegyeinek összege: {sod}')

# sum_of_digits()

# 3. feladat
""" Kérj be egy mondatot, és írd ki a szavait visszafelé sorrendben, de a szavak betűit ne fordítsd
meg! """
def reverse_sentence():
    sentence = input("írj be egy mondatot: ")
    sentence_split = sentence.split(" ")
    sentence__split_reversed = reversed(sentence_split)
    print(" ".join(sentence__split_reversed))
    # print(" ".join(sentence_split[::-1]))

# reverse_sentence()

#4. feladat
""" Kérj be számokat egy listába (Enterrel lezárható), majd írd ki, melyik szám szerepelt a
legtöbbször, és hányszor! """
# Ez végül nem biztos, hogy a legeffektívebb megoldás lett, de elsőre jó ötletnek tűnt és gondoltam már végigviszem, ha belekezdtem :D
def most_frequent_value():
    values = []
    value = input("Adj meg egy számot: ")

    while value:
        values.append(int(value))
        value = input("Adj meg egy számot: ")

    values_dict = {}
    for element in values:
        if element not in values_dict:
            values_dict[element] = 1
        else:
            values_dict[element] += 1

    highest_freq = 0
    for element in values_dict:
        # print(f'{element} : {values_dict[element]}')
        if values_dict[element] > highest_freq:
            highest_freq = values_dict[element]

    # print(f'Highest frequency: {highest_freq}')
    # print("Legtöbbször az alábbi szám(ok) fordul(nak) elő: ")
    highest_values = []
    for element in values_dict:
        if values_dict[element] == highest_freq:
            highest_values.append(str(element))
            # print(element)
    # print(f'összesen {highest_freq}x.')
    print(f'Legtöbbször a(z) {", ".join(highest_values)} szám(ok) fordul(nak) elő. Gyakoriságuk: {highest_freq}')
    # print(highest_values)

# most_frequent_value()

# 5. feladat
""" Írj egy függvényt, ami bekér egy jelszót, és eldönti, hogy elég erős-e!
A jelszó akkor erős, ha:
 Legalább 8 karakter hosszú
 Tartalmaz számot
 Tartalmaz nagybetűt
 Tartalmaz kisbetűt
Tipp: használhatsz any(c.isdigit() for c in jelszo) jellegű megoldást. """
def strong_pwd():
    pwd = input("Jelszó (min 8 karakter, 1 nagy, 1 kis betű, 1 szám): ")
    is_long = False
    contains_upper = False
    contains_lower = False
    contains_number = False

    print(f'length: {len(pwd)}')

    if len(pwd) >= 8:
        is_long = True
    i = 0
    while (not contains_upper or not contains_lower or not contains_number) and i < len(pwd):
        # print(i)
        if pwd[i].isupper():
            print(f'{pwd[i]} is uppercase')
            contains_upper = True
        if pwd[i].islower():
            print(f'{pwd[i]} is lowercase')
            contains_lower = True
        if pwd[i].isdigit():
            print(f'{pwd[i]} is digit')
            contains_number = True
        i += 1

    if contains_upper and contains_lower and contains_number and is_long:
        print(f'{pwd} is a strong password')
    else:
        missing_criteria = []
        if not contains_upper:
            missing_criteria.append("upper case character")
        if not contains_lower:
            missing_criteria.append("lower case character")
        if not contains_number:
            missing_criteria.append("number")
        if not is_long:
            missing_criteria.append(str(8 - len(pwd)) + " additional characters")
        print(f'"{pwd}" is not a strong password. It is missing: {", ".join(missing_criteria)}.')

# strong_pwd()