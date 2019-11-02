#Utwórz program do zamiany kilometrów na mile i na odwrót. 

  

def km_na_m(v): 

    return v*1.609344 

def m_na_km(v): 

    return  v/1.609344 

  

print("Jest to program, który zmienia kilmotery na mile i na odwrót") 

print("km->m (wprowadź 1), m->km (wprowadż 2)") 

decyzja=int(input ()) 

  

if (decyzja == 1): 

    print("wprowadz prędkosć") 

    v= float(input()) 

    wynik= km_na_m(v) 

    print(wynik) 

     

if(decyzja==2): 

    print("wprowadz prędkosć") 

    v= float(input()) 

    wynik= m_na_km(v) 

    print(wynik)