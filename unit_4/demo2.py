# c = "a"
# print(c, ord(c), hex(ord(c)), c.encode())
#
#
# print()
# c = "\u20AC"
#
# print(c, ord(c), hex(ord(c)), c.encode())

alphabet = ""

for i in range(ord("a"), ord("z") + 1):
    alphabet += chr(i)


print(alphabet.index("w"))
print("aAbByYzZAa".index("A"))
print([1, 2, 3].index(3))

print(list(alphabet))
print(alphabet.count(("a")))
print("Ala ma kota".count("a"))
print([1, 2, 2, 3, 4].count(1))