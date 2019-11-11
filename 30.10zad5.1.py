#Utwórz skrypt z interfejsem tekstowym który obliczy silnię od danego argumentu. Wykonać zadanie na dwa sposoby – iteracyjnie i rekurencyjnie. 
def silnia(n): 

    s=1 

    for i in range(1, n+1): 
        s=s*i 
    return s 
  

def silnia_r(n):      
    if(n==1): 
        return 1 

    else: 
        return n*silnia_r(n-1)   #w obrebie funkcji odwołuje się do niej samej 