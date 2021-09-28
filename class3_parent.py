class Person:
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2

    def eat(self):
        print("냠냠")

    def sleep(self):
        print("쿨쿨...")

    def talk(self):
        print("Talking !")


class Yeong(Person):
    def study(self):
        print("Study hard!")


yeongmin = Yeong()
print(f"영민이의 눈은 {yeongmin.eyes}개!")
