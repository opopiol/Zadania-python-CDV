#Napisz skrypt, który będzie wyświetlać wszystkie kolejne dzielniki wprowadzonej liczby:
print("Jest to program, który wywietla wszystkie kolejne dzielniki wprowadzonej liczby") 

print("wprowadz liczbe: ") 

n=int(input ()) 


for i in range(2,n+1):  

    if(n%i==0): 

        print(i) 