class Car():
    tires = 4
    windows = 4
    handle = 1
    seats = 4


class Ferrari_Car(Car):
    expense = 200000000
    brand = "Ferrari"


class Hyundai_Car(Car):
    expense = 30000000
    brand = "Hyundai"


print(
    f"자동차의 기본 요소중 핸들은 {Car.handle}개, 좌석은 {Car.seats}개, 창문은 {Car.windows}개, 타이어는 총 {Car.tires}개 있다.")
print(
    f"그 중 유명한 현대자동차와 페라리가 있는데, 페라리의 평균 차량 시세는 {Ferrari_Car.expense}원이고, 현대차의 평균 시세는 {Hyundai_Car.expense}원이다.")
