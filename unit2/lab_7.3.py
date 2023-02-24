import random

number = random.randint(1, 10)
msg = "Zgadnij liczbę od 1 do 10: "

guess = int(input(msg))

if guess == number:
    print("Brawo!")
else:
    print("Źle, ta liczba jest:")
    if number % 2 == 0:
        print("-parzysta")
    else:
        print("-nieparzysta")
    msg = "Zgaduj dalej: "
    guess = int(input(msg))
    if guess == number:
        print("Brawo!")
    else:
        print("Dalej źle, ta liczba jest:")
        if number > 5:
            print("- większa od 5")
        else:
            print("- mniejsza od 5")
        msg = "Ostatnia szansa: "
        guess = int(input(msg))
        if guess == number:
            print("Nareszcie się udało!")
        else:
            print("Niestety nie zgadłeś.")
