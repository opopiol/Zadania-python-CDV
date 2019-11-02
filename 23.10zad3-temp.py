#Korzystając z pojęcia funkcji utwórz program, który będzie miał możliwość zamiany temperatury pomiędzy skalami Celsjusza i Fahrenheita (w obie strony). C = (F-32)x(5/9), F = (C*9/5)+32 


def CnaF(temp): 

    return (temp*9/5)+32 


def FnaC(temp): 

    return (temp-32)*(5/9) 


print("Jest to program, który moze zmeinic skale temperatury pomiędzy skalami Celsjusza i Fahrenheita") 

print("C->F (wprowadź 1), F->C (wprowadż 2)") 

decyzja=int(input ()) 

  
if(decyzja == 1): 

    print("wprowadz temperature") 

    temp= float(input()) 

    wynik= CnaF(temp) 

    print(wynik) 
    

if(decyzja == 2): 

    print("wprowadz temperature") 

    temp= float(input()) 

    wynik= FnaC(temp) 

    print(wynik) 