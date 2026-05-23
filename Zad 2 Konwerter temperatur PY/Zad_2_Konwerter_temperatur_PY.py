print("=== KONWERTER TEMPERATUR ===\n")

try:
    kierunek = input("Wybierz konwersję (C - Celsjusz→Fahrenheit, F - Fahrenheit→Celsjusz): ").upper()
    temperatura = float(input("Podaj temperaturę: "))

    if kierunek == 'C':
        fahrenheit = temperatura * 1.8 + 32
        print(f"{temperatura}°C = {fahrenheit}°F")
    elif kierunek == 'F':
        celsjusz = (temperatura - 32) / 1.8
        print(f"{temperatura}°F = {celsjusz}°C")
    else:
        print("Błąd: Wybierz C lub F!")

except ValueError:
    print("Błąd: Wprowadź prawidłową wartość temperatury!")
