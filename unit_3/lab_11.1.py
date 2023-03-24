import random

guess_numbers = []
numbers = []
counter = 0

for i in range(6):
    guess_numbers.append(int(input("Podaj liczbę: ")))


for i in range(6):
    numbers = random.sample(range(1, 50), 6)

for number in guess_numbers:
    if number in numbers:
        counter += 1

guess_numbers.sort()
numbers.sort()


print("Podane liczby:", guess_numbers)
print("Wylosowane liczby:", numbers)
print("Trafiono", counter, "razy.")