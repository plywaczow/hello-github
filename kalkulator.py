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