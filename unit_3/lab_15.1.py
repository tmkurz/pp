def safe_int():
    arg = input("Podaj argument: ")
    try:
        arg = int
        print(arg)
    except:
        None



safe_int()
