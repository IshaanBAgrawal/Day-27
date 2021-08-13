def add(*nums):
    answer = 0
    for num in nums:
        answer += num
    return answer


# print(add(1, 2, 3))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.highest_speed = kw.get("highest_speed")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
print(my_car.make)
print(my_car.highest_speed)
