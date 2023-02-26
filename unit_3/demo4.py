#przykład 1
# def sum_numbers(numbers):
#     sum = 0
#     for element in numbers:
#         sum += element
#
#     return sum
#
# print(sum_numbers([1, 2, 3]))
#
#
# sum_numbers(1)

# #przykład 2
# def scope_test():
#     global x
#     x = 55
#     print("w środku funkcji: " + str(x))
#
# x = 123
# scope_test()
# print("Na zawnątrz: " +str(x))

#przykład 3

# def change_value(n):
#     print("Przed zmianą: ", n)
#     n[0] = 99
#     print("po zmianie: ", n)
#
# val = [1, 2]
# change_value(val)
# print(val)

#przykład 3
def recursion(number):
    if number == 20:
        return
    print(number)
    number += 1
    recursion(number)

recursion(5)