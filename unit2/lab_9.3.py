number = int(input("Podaj liczbę całkowitą: "))
n_bit = int(input("Podaj numer bitu: "))

mask = 1 << n_bit

result = number & mask

bit = int(bool(result))

print(bit)