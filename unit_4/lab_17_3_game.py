from games.lotto import get_user_numbers, check_numbers, draw_numbers

print("Witaj w grze LOTTO!")
user_numbers = get_user_numbers()
print("Podane liczby to: ", user_numbers)

print("\nNaciśnij ENTER, aby wylosować liczby.\n")
input()
lucky_numbers = draw_numbers()
print("Wylosowane liczby to:", lucky_numbers)

result = check_numbers(user_numbers, lucky_numbers)
if result == 6:
    print("Gratulacje! Trafiłeś 6.")
elif result == 5:
    print("Trafiłeś 5!")
elif result == 4:
    print("Trafiłeś 4!")
elif result == 3:
    print("Trafiłeś 3!")
elif result == 2 or 1:
    print("Trafiłeś ", result, " razy, było blisko.")
else:
    print("Niestety nie trafiłeś.")

