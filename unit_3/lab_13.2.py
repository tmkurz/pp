def table(a, b):
    print(a, "x", b, "=", a * b)
    if a == 10 and b == 10:
        return
    elif a == 10:
        table(1, b + 1)
    else:
        table(a + 1, b)

table(1, 1)