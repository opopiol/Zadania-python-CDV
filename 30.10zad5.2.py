#Utwórz skrypt z interfejsem tekstowym który obliczy silnię od danego argumentu. Wykonać zadanie na dwa sposoby – iteracyjnie i rekurencyjnie. 
silnia=1 
 

print('Program do obliczania silni: ') 
print("Podaj liczbę: ") 
n=int(input()) 
    

for i in range(1,n+1): 
    silnia=silnia*i 
print("Silnia wynosi {}".format(silnia)) 
     

if(n<0): 
    print("nie można wykonać") 
  

elif(n==0): 
    print("1") 