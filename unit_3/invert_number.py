while True:
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        print("Odwrota liczba to", 1/ number)
    except ValueError:
        print("To nie jest liczba całkowita.")
    except ZeroDivisionError:
        print("Błąd dzielenia przez zero.")
    except:
        print("Coś poszło nie tak.")
