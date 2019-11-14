#Zadanie 6. 
#Utworzyć skrypt z interfejsem tekstowym obliczający n-ty element ciągu Fibonacciego – wykonać zadanie iteracyjnie i rekurencyjnie. 

def fib_r(n):
    if n == 1:
            return 1
    elif n == 2:
            return 1
    else:
            return fib_r(n - 1) + fib_r(n - 2)

def fib(x):
    f1=0
    f2=1
    for i in range(1,x):
        f=f1+f2
        f1=f2
        f2=f
    return f2 


x=int(input("Wpisz którego elementu ciągu szukasz: "))
print("Element wynosi: {}".format(fib(x)))