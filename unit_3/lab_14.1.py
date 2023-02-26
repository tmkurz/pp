phones = {"Tomek": 15365,
          "Karol": 63258,
          "Ola": 75236,
          "Damian": 95632
          }


name = input("Podaj imię: ")


if name in phones:
    print("Numer telefonu to :", phones[name])
else:
    print("Brak numeru")
