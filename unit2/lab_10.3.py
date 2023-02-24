numbers = [1, 5, 5, 7, 9, 5, 8, 5]
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for number in numbers:
    frequency[number] += 1

print(frequency)

most_common = -1
for i in range(len(frequency)):
    if frequency[i] > most_common:
        most_common = i

print("Najczęściej występuje " + str(most_common) + " - " + str(frequency[most_common]) + " razy.")