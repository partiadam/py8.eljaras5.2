'''
5.2 Feladat
A program, egy eljárás segítségével kirajzol a képernyőre egy 6x3-as mezőt. Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak megfelelően a program az adott pozícióba 'O' helyett '+' jelet írjon ki. A lenti példában az eljárás hivása: mezot_rajzol(0,4)

    O O O O + O
    O O O O O O
    O O O O O O

Feladat
Alakítsd át az előző programot úgy, hogy a felhasználó adhassa meg a koordinátákat, ahová a program 'O' helyett '+' jelet ír. A koordináták bekérése és a mező kirajzolása addig ismétlődjön, amíg a felhasználó negatív számot nem ad meg koordinátaként!
'''


 
def mezot_rajzol():
    szel = int(input('adj meg x koordinátát: (0-tól): \t'))
    hossz = int(input('adj meg y koordinátát (0-tól): \t'))
    for sor in range(3):
        for oszlop in range(6):
            if oszlop == szel and hossz == sor:
                print('+ ', end='')
                szel +=10
            else:
                print('O ', end='')
        print()

mezot_rajzol()