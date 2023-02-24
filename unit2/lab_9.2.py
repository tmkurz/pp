counter = 0

for i in range(1, 101):
    if (i % 2 == 0 and i > 90) or (i % 2 != 0 and i % 9 == 0):
        counter += 1
print("Liczb, które są parzyste i większe od 90, a gdy są nieparzyste, to dzielą się przez 9 jest " + str(counter) + ".")