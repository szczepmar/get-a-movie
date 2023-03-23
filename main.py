import scrap
import operacje_z_baza_filmow
import os
os.system('cls||clear')
ui = '''
--------------------------------
Nacisnij przyciski (1,8,0), aby wybrac co ciebie interesuje
1. Wylosuj film
8. Stwórz bazę danych ze strony filmweb.pl(top 500) 
0. Wyjście
'''
exit = True
while exit == True:
    decision = int(input(ui))
    os.system('cls||clear')
    if decision == 1:
        operacje_z_baza_filmow.random_movie()
    elif decision == 8:
        scrap.scrap()
    elif decision == 0:
        print("Do zobaczenia później")
        exit = False
    else:
        print("Coś poszło nie tak\n")
