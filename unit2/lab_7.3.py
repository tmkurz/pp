import random

number = random.randint(1, 10)
msg = "Zgadnij liczbę od 1 do 10: "

guess = int(input(msg))

if guess == number:
    print("Brawo!")
else:
    print("Źle, ta liczba jest")
    if number % 2 == 0:
        print("-parzysta")
    else:
        print("-nieparzysta")
    msg = "Zgaduj dalej: "
    guess = int(input(msg))
    if guess == number:
        print("Brawo!")