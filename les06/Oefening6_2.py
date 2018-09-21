getallenlijst = [2, 4, 6, 8, 10, 9, 7]

zoekgetal = int(input('Geef getal: '))
gevonden = False


for getal in getallenlijst:
    if getal == zoekgetal:
        gevonden = True

if gevonden:
    print('het zoekgetal zit in de getallenlijst')

