range_from = int(input("Podaj początek zakresu: "))
range_to = int(input("Podaj koniec zakresu: "))

for i in range(range_from, range_to + 1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i)
