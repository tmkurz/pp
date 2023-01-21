print('Podaj znak: ')
znak = input()

print('Podaj liczbę kolumn: ')

kolumny = int(input())

print('Podaj liczbę wierszy: ')

wiersz = int(input())

print((str(znak) * wiersz + "\n") * kolumny)