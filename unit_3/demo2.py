# # numbers = [10, 8, 6, 3, 2]
# #
# # # print(5 not in numbers)
# #
# numbers = [i for i in range(1, 64) if i % 1 == 0 and i % 2 == 0]
# # for i in range(1, 1001):
# #     numbers.append(i)
#
# print(numbers)

# print(len([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]))

numbers = [1, 2, 3]
l2 = [numbers[:], 7]

numbers[0] = 99
print(numbers)
print(l2)