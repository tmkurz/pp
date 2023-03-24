def print_char(char="*", rep=10, vert=False):
    for i in range(rep):
        if vert:
            print((char))
        else:
            print(char + " ", end="")
    print()

print_char("&", 7, True)



