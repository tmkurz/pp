class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def introduce(self):
        print("Cześć, jestem", self.__name, ", mam", self.__age, "lat.")



obj1 = Person("Jan", 25)
obj2 = Person("Ania", 30)

print(obj1.introduce())
print(obj2.introduce())


