
import math
from datetime import datetime


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
        raise ValueError("Nie można obliczyć pierwiastka z liczby ujemnej.")
    return math.sqrt(a)


def modulo(a, b):
    if b == 0:
        raise ValueError("Nie można obliczyć modulo przez zero.")
    return a % b


def procent(a, b):
    return a * b / 100


def pobierz_liczbe(komunikat):
    while True:
        tekst = input(komunikat).strip().replace(",", ".")
        try:
            liczba = float(tekst)
            if not math.isfinite(liczba):
                print("Podaj skończoną liczbę.")
                continue
            return liczba
        except ValueError:
            print("Błąd! Wpisz poprawną liczbę.")


def pokaz_menu():
    print("""
================================
       KALKULATOR PYTHON
================================
+   Dodawanie
-   Odejmowanie
*   Mnożenie
/   Dzielenie
^   Potęgowanie
sqrt Pierwiastek kwadratowy
%   Modulo (reszta z dzielenia)
pct Procent z liczby
hist Historia obliczeń
clear Wyczyść historię
0   Zakończ program
================================
""")


def menu():
    historia = []

    while True:
        pokaz_menu()
        dzialanie = input("Wybierz działanie: ").strip().lower()

        if dzialanie == "0":
            print("Dziękuję za korzystanie z kalkulatora!")
            break

        if dzialanie == "hist":
            if historia:
                print("\n--- Historia obliczeń ---")
                for i, wpis in enumerate(historia, start=1):
                    print(f"{i}. {wpis}")
            else:
                print("Historia jest pusta.")
            input("\nNaciśnij Enter, aby kontynuować...")
            continue

        if dzialanie == "clear":
            historia.clear()
            print("Historia została wyczyszczona.")
            continue

        try:
            a = pobierz_liczbe("Podaj pierwszą liczbę: ")

            if dzialanie == "sqrt":
                wynik = pierwiastek(a)
                opis = f"√{a} = {wynik}"

            elif dzialanie in ("+", "-", "*", "/", "^", "%", "pct"):
                b = pobierz_liczbe("Podaj drugą liczbę: ")

                if dzialanie == "+":
                    wynik = dodaj(a, b)
                elif dzialanie == "-":
                    wynik = odejmij(a, b)
                elif dzialanie == "*":
                    wynik = pomnoz(a, b)
                elif dzialanie == "/":
                    wynik = podziel(a, b)
                elif dzialanie == "^":
                    wynik = potega(a, b)
                elif dzialanie == "%":
                    wynik = modulo(a, b)
                else:
                    wynik = procent(a, b)

                opis = f"{a} {dzialanie} {b} = {wynik}"

            else:
                print("Nieznane działanie. Wybierz opcję z menu.")
                continue

            if isinstance(wynik, complex):
                print("Wynik:", wynik)
            elif isinstance(wynik, float) and not math.isfinite(wynik):
                print("Wynik jest poza obsługiwanym zakresem.")
                continue
            else:
                print(f"Wynik: {wynik:.10g}")

            historia.append(
                f"{datetime.now():%H:%M:%S} | {opis}"
            )

        except (ValueError, OverflowError) as blad:
            print(f"Błąd: {blad}")

        input("\nNaciśnij Enter, aby wykonać kolejne działanie...")


if __name__ == "__main__":
    menu()
