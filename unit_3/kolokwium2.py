#Pobierz od użytkownika trzy liczby całkowite reprezentujące długości odcinków i sprawdź czy jest możliwe zbudowanie z tych odcinków dowolnego trójkąta.

a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))
c = int(input("Podaj trzecią liczbę całkowitą: "))

if (a + b > c) or (a + c > b) or (b + c > a):
    print("Z podanych liczb można zbudować trójkąt.")
else:
    print("Z tych liczb nie można zbudować trójkąta.")