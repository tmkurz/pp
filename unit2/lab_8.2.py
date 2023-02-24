number = int(input("Podaj rozmiar: "))
sign = input("Podaj znak: ")

for i in range(number):
    for j in range(number):
        print(sign, end=" ")
    print()