def calc(numbers, exponent):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers

print(calc([2, 4, 5], 2))


