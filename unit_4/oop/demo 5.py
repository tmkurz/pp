class MyClass:
#     def __my_private_method(self):
#         print("To jest metoda prywatna")
#     def my_public_method(self):
#         self.__my_private_method()
#         print("To jest metoda publiczna")
#
# obj = MyClass()
#
# obj.my_public_method()
# print()
#
# print(obj.__dict__)
# print(MyClass.__dict__)
#
# print()
# print(MyClass.__name__)
# print((type(obj).__name__))
#
# print()
# print(MyClass.__module__)
#
    x = 5

    def __init__(self):
        self.y = 9

obj = MyClass()
print((obj.x, obj.y))

print(MyClass.__dict__)
print(obj.__dict__)

setattr(obj, "z", 1)
print(getattr(obj, "x"))

print("z: ", obj.z)