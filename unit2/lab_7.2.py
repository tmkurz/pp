score = int(input("Ilość otrzymanych punktów (0-100): "))
if score >= 95:
    print("Ocena bardzo dobra 5,0")
elif score > 84:
    print("Ocena ponad dobra 4,5")
elif score >= 70:
    print("Ocena dobra 4,0")
elif score > 60:
    print("Ocena dość dobra 3,5")
elif score > 50:
    print("Ocena dostateczna 3,0")
else:
    print("Ocena niedostatczna 2,0")
