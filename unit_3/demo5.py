#krotki
# numbers = (1, 2, 3)
# numbers = 1, 2, 3
#
# numbers = ()
#
# numbers = [1, 2, 3]
# print(numbers)
# numbers = tuple(numbers)
#
# print(numbers)

# #słowniki
# phones = {"Tomek": 351553145, "Ada": 15154721, "Karol": 848153513}
#
# print(phones)

animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "lis": "fox"
}

words = ["kot", "lew", "lis"]
#
# for word in words:
#     if word in animals_dict:
#         print(word, "->", animals_dict[word])
#     else:
#         print("Nie ma słowa" , word, " w słowniku.")

# for key in animals_dict.keys():
#     print(key, "->", animals_dict[key])
#
# for pl, en in animals_dict.items():
#     print(pl, "->", en)

animals_dict["świnka"] = "pig"

print(animals_dict)

animals_dict.update({"świnka": "piggy"})

print(animals_dict)

dict2 = animals_dict.copy()

del dict2["świnka"]
print(dict2)