class Amazon:
    strength = 20
    dexterity = 25
    vitality = 20
    energy = 15

    def attack(self):
        return "Attacked!!!"

    def exercise(self):
        self.strength += 2
        self.dexterity += 3
        self.vitality += 1


jane = Amazon()  # Create a Jane to character
mary = Amazon()  # Create a Mary to character

print(jane.strength)
print(jane.attack())
print(mary.vitality)

for i in range(5):
    print(mary.attack())

print(jane.strength)
jane.exercise()
print(jane.strength)
jane.exercise()
print(jane.strength)
