import math
def dodaj(a, b):
    return a + b
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
def modulo(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero.")
    return a % b
def silnia(a):
    if a < 0 or not float(a).is_integer():
        raise ValueError("Silnię można policzyć tylko z nieujemnej liczby całkowitej.")
    return math.factorial(int(a))
def menu():
    print("=== Kalkulator ===")
    jednoargumentowe = ("sqrt", "!")
    dozwolone = ("+", "-", "*", "/", "^", "%", "sqrt", "!")
    while True:
        dzialanie = input("\nDziałanie (+, -, *, /, ^, %, sqrt, !) lub 'q' aby wyjść: ").strip()
        if dzialanie.lower() in ("q", "koniec"):
            print("Koniec pracy kalkulatora.")
            break

        if dzialanie not in dozwolone:
            print("Nieznane działanie")
            continue

        try:
            a = float(input("Podaj liczbę: " if dzialanie in jednoargumentowe else "Podaj pierwszą liczbę: "))
            if dzialanie == "sqrt":
                print("Wynik:", pierwiastek(a))
            elif dzialanie == "!":
                print("Wynik:", silnia(a))
            else:
                b = float(input("Podaj drugą liczbę: "))
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
                elif dzialanie == "%":
                    print("Wynik:", modulo(a, b))
        except ValueError as e:
            print("Błąd:", e)


if __name__ == "__main__":
    menu()
