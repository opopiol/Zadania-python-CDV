#Korzystając z pętli for oraz możliwości formatowania działania funkcji print utwórz program, który po prowadzeniu liczby wyświetli następujący komunikat: 

print("Jest to program, który wyswietla wartosci mnozenia") 

print("podaj liczbe : ") 

liczba=int(input ()) 


for i in range(1, 11): 

    liczba1=float(liczba) 
  

    print("{0} x {1} = {2}". format(liczba1, i, liczba1*i)) 