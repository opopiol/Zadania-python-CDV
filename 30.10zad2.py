#Zadanie 2.  
#W klasie przeprowadzono sprawdzian, za który uczniowie mogli otrzymać maksymalnie 40 punktów. Skala ocen w szkole jest następująca: 0-39% - ndst, 40-49% - dop, 50-69% - dst, 70-84% - db, 85-99% - bdb, 100% - cel. Utwórz skrypt z interfejsem tekstowym, który na podstawie podanej liczby punktów ze sprawdzianu wyświetli ocenę jaka się należy (skorzystaj z konstrukcji if, elif, else).  
  

print("Wyswiewtla oceny")    
print( "podaj ilosc punktow") 
  
pkt=int(input()) 
max_pkt=40 
proc=(pkt/max_pkt)*100 

  
print("uzsykany procent: {}%".format(proc)) 
  

if(proc>=0 and proc<40): 
    print("uzsykana ocena: ndst") 

elif(proc>=40 and proc<50): 
    print("uzsykana ocena: dop") 

elif(proc>=50 and proc<70): 
    print("uzsykana ocena: dst") 

elif(proc>=70 and proc<85): 
    print("uzsykana ocena: db") 

elif(proc>=85 and proc<=99): 
    print("uzsykana ocena: bdb") 

elif(proc==100): 
    print("uzsykana ocena: cel") 

elif(proc<0 or proc>100): 
    print("p0za skalą") 