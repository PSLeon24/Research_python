# object in object!

# How to put elephant in refrigerator?
# Step 1. Open the refrigerator.
# Step 2. put in!
# Step 3. Close the refrigerator.

# Coding NOOOW!

class Frige:
    def __init__(self):
        self.isOpend = False
        self.foods = []

    def open(self):
        self.isOpend = True
        return "Open the refrigerator!"

    def put(self, thing):
        if self.isOpend == True:
            self.foods.append(thing)
            return "Put in the thing!"
        else:
            return "Plz, Open the refrigerator!"

    def close(self):
        self.isOpend = False
        return "Close the refrigerator!"


class Food:
    pass


class Elephant:
    pass


my_fridge = Frige()
apple = Food()
orange = Food()
elephant = Elephant()

my_fridge.put(apple)
my_fridge.open()
my_fridge.put(elephant)
my_fridge.close()

print(my_fridge.foods)
