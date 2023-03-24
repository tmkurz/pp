numbers = []
numbers_total = int(input("Podaj liczbę elementów zbioru: "))

for i in range(numbers_total):
    number = int(input("Podaj liczbę całkowitą: "))
    numbers.append(number)

numbers.sort(reverse=True)

numbers_final = []

for number in numbers:
    if number not in numbers_final:
        numbers_final.append(number)

print(numbers_final)