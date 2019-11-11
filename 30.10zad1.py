#Utwórz skrypt z interfejsem tekstowym, który pobierze od użytkownika zdanie i wyświetli w kolejnych wierszach litery tego zdania w odwróconej kolejności. 

print( "podaj zdanie") 
zd=input() 


dl_zd=len(zd)-1 


for i in range(0,dl_zd+1): 

    print(zd[dl_zd-i]) #w kwadratowym bo  chcemy aby pokazywał poszczególne litery 