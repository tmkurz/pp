class MyClass:
    pass

my_obj = MyClass()
my_obj.x = 5

print(my_obj.x)

print(type(my_obj))

my_obj2 = MyClass()
my_obj2.x = 99

print(my_obj2.x)
print(my_obj.x, my_obj2.x)