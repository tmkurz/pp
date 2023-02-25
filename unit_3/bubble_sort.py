numbers = [5, 4, 2, 1, 8, 90, 67, 43, 2]
swapped = True

while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True

print(numbers)

numbers.sort(reverse=True)
print(numbers)
