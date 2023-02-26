numbers = []
counter = 0


while True:
    if counter > 4:
        break
    try:
        n = int(input("Podaj liczbę całkowitą: "))
        counter += 1
    except:
        print("To ie jest liczba całkowita!")
print(numbers)