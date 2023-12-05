# 1. Create a singleton class
class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


# 2. Create a class with Singleton metaclass
class PrintObject(metaclass=Singleton):
    def __init__(self):
        print("This is called by super().__call__()")


# 3. Create a singleton object
obj1 = PrintObject()
obj2 = PrintObject()

print(obj1)
print(obj2)
print(obj1 is obj2)  # Result is True, so obj1 and obj2 are the same object.
