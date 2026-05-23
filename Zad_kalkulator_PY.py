print("=== KALKULATOR DWÓCH LICZB ===\n")

def format_and_print(wynik):
    if isinstance(wynik, float) and wynik.is_integer():
        print(f"Wynik: {int(wynik)}")
    else:
        print(f"Wynik: {wynik}")

try:
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    operacja = input("Wybierz operację (+, -, *, /): ")

    if operacja == '+':
        wynik = liczba1 + liczba2
        format_and_print(wynik)
    elif operacja == '-':
        wynik = liczba1 - liczba2
        format_and_print(wynik)
    elif operacja == '*':
        wynik = liczba1 * liczba2
        format_and_print(wynik)
    elif operacja == '/':
        if liczba2 != 0:
            wynik = liczba1 / liczba2
            format_and_print(wynik)
        else:
            print("Błąd: Nie można dzielić przez zero!")
    else:
        print("Błąd: Nieprawidłowa operacja!")

except ValueError:
    print("Błąd: Wprowadź prawidłowe liczby!")
