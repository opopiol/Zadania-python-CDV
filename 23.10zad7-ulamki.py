#Utwórz program dodający ułamki zwykłe

print('Dodawanie ułamków zwykłych')

licznik1=int(input('Podaj licznik1: '))
mianownik1=int(input('Podaj mianownik1: '))
licznik2=int(input('Podaj licznik2: '))
mianownik2=int(input('Podaj mianownik2: '))

from fractions import Fraction 
wynik= (Fraction(licznik1,mianownik1) + Fraction(licznik2,mianownik2))

print(wynik) 