"""
1. feladat: ket szam syorzata, ha nem szamot kapunk fusson hibara
"""

def szorzat():
    # szam1 = int(input("Adj meg egy szamot: "))
    # szam2 = int(input("Adj meg megegy szamot: "))
    szam1 = input("Adj meg egy szamot: ")
    szam2 = input("Adj meg megegy szamot: ")
    if szam1.isdigit() and szam2.isdigit():
        print(f'{szam1} es {szam2} szorzata: {int(szam1) * int(szam2)}')
    else:
        print("nem szamot adtal meg")
# szorzat()

""" 
2. feladat: a kisebb szam duplaja
"""
def kisebb_dupla():
    szam1 = int(input("Adj meg egy szamot: "))
    szam2 = int(input("Adj meg megegy szamot: "))
    kisebb = int()
    if szam1 < szam2:
        kisebb = szam1
    else:
        kisebb = szam2
    print(f'A kisebb ({kisebb} duplaja: {kisebb * 2})')
# kisebb_dupla()

""" 
3. feladat: paros-paratlan
"""

def paros_paratlan():
    szam = int(input("Adj meg egy egesz szamot: "))
    if szam % 2 == 0:
        print(f'Ez a szam ({szam}) paros.')
    else:
        print(f'Ez a szam ({szam}) paratlan.')
# paros_paratlan()

""" 
4. feladat: a nagyobb haromszorosa
"""
def nagyobbTripla():
    szam1 = int(input("Adj meg egy szamot: "))
    szam2 = int(input("Adj meg megegy szamot: "))
    nagyobb = int()
    if szam1 > szam2:
        nagyobb = szam1
    else:
        nagyobb = szam2
    print(f'A ket szam kozul a nagyobb ({nagyobb}) haromszorosa ({nagyobb * 3}).')
# nagyobbTripla()

"""
5. feladat: szokozok nelkul
"""
def szokozok_nelkul():
    szoveg = input("Adj meg egy szovget szokozokkel: ")
    szoveg_szokozok_nelkul = szoveg.replace(' ', '')
    print(f'A "{szoveg}" szokozok nelku "{szoveg_szokozok_nelkul}"')
# szokozok_nelkul()