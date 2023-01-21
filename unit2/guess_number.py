import random

number = random.randint(1, 3)

guess = int(input("Zgadnij jaką liczbę mam na myśli (1, 2 lub 3): "))
if guess == number:
    print("Brawo! Taką liczbę miałem na myśli.")
else:
    print("Chodziło o liczbę " + str(number) + ".")