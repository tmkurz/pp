import random
rolls = []
rolls_total = 16

for i in range(rolls_total):
    rolls.append(random.randint(1, 6))

print("Wyniki po ", rolls_total, "rzutach: ", rolls)
print("Za 8 razem wypadło: ", rolls[7])

sixes = 0

for j in rolls:
    if j == 6:
        sixes += 1

print("Szóstka wypadła " + str(sixes) + " razy.")

in_row_value_tmp = rolls[0]
in_row_total_tmp = 0
in_row_value = 0
in_row_total = 0

for k in rolls:
    if k == in_row_value_tmp:
        in_row_total_tmp += 1
    else:
        in_row_value_tmp = k
        in_row_total_tmp = 1
    if in_row_total_tmp > in_row_total:
        in_row_total = in_row_total_tmp
        in_row_value = in_row_value_tmp

print("Z rzędu wyrzucono", in_row_total, "razy wartość " + str(in_row_value) + ".")