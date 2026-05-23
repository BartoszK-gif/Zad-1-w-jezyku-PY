print("=== ŚREDNIA OCEN UCZNIA ===\n")

try:
    liczba_ocen = int(input("Podaj liczbę ocen: "))

    if liczba_ocen <= 0:
        print("Błąd: Liczba ocen musi być większa od zera!")
    else:
        suma_ocen = 0

        for i in range(liczba_ocen):
            ocena = float(input(f"Podaj ocenę {i + 1}: "))
            if ocena < 1 or ocena > 6:
                print("Uwaga: Ocena powinna być w zakresie 1-6")
            suma_ocen += ocena

        srednia = suma_ocen / liczba_ocen
        print(f"\nŚrednia: {srednia:.2f}")

        if srednia >= 3.0:
            print("Uczeń zdał.")
        else:
            print("Uczeń nie zdał.")

except ValueError:
    print("Błąd: Wprowadź prawidłowe wartości!")
