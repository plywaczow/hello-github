import math
def dodaj(a, b):
    return a - b
def odejmij(a, b):
    return a - b
def pomnoz(a, b):
    return a * b
def podziel(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero.")
    return a / b
def potega(a, b):
    return a ** b
def pierwiastek(a):
    if a < 0:
        raise ValueError("Nie można liczyć pierwiastka z liczby ujemnej")
    return math.sqrt(a)
def menu():
    print("=== Kalkulator ===")
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    dzialanie = input("Działanie (+, -, *, / ,^ ,sqrt): ")
    if dzialanie == "+":
        print("Wynik:", dodaj(a, b))
    elif dzialanie == "-":
        print("Wynik:", odejmij(a, b))
    elif dzialanie == "*":
        print("Wynik:", pomnoz(a, b))
    elif dzialanie == "/":
        print("Wynik:", podziel(a, b))
    elif dzialanie == "^":
        print("Wynik:", potega(a, b))
    elif dzialanie == "sqrt":
        print("Wynik:", pierwiastek(a))
    else:
        print("Nieznane działanie")



if __name__ == "__main__":
    menu() 