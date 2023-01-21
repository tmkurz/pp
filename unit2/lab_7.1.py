number = int(input("Podaj liczbę całkowitą: "))

if (number ** .5) % 1 == 0:
    str1 = "Tak"
    str2 = ""
else:
    str1 = "Nie"
    str2 = "nie"

print(str1 + ", pierwiastek kwadratowy z liczby " + str(number) + " " + str2 + "jest liczbą całkowitą.")