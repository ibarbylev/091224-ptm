from typing import Callable


class CallableCar:
    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year

    def __call__(self, *args, **kwargs):
        print(f"Model: {self.model}, year: {self.year} is the best!!!")

    def __str__(self):
        return f"Car(model={self.model}, year={self.year})"


car = CallableCar('WV', 2022)
print(car)  # Car(model=WV, year=2022)
car()       # Model: WV, year: 2022 is the best!!!

print(isinstance(car, Callable))  # True
