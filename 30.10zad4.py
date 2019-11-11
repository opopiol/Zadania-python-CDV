#Utwórz skrypt z interfejsem tekstowym, który przyjmie od użytkownika ile elementów chce on wprowadzić do listy, przyjmie te elementy, a następnie wyliczy: średnią i odchylenie standardowe średniej. Wykonać zadanie na dwa sposoby: poprzez utworzenie funkcji własnych obliczających średnią i odchylenie standardowe oraz korzystając z gotowych funkcji np. z pakietu numpy. 


print("podaj liczbę elementów") 
n=int(input()) 
tab=[] 

print("Podaj dane") 

  
for i in range(0,n): 
    tab.append(float(input())) 
    
srednia=sum(tab)/n 
  
print("Srednia wynosi {}".format(srednia)) 