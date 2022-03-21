class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        # Python suggests this is a better way versus the practice below
        if not isinstance(car, Car):
            raise ValueError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
        self.cars.append(car)



ford = Garage()
fiesta = Car('Ford', 'Fiesta')

try:
    ford.add_car('Fiesta')
except TypeError:
    print('Your car was not a car!')
except ValueError:
    print('Something weird happened...')
finally:
    print(f'The garage now has {len(ford)} cars.')  # the finally block always runs.

"""
# NOT common practice to write program like this...Ask permission first, then run code
if isinstance(fiesta, Car):
    ford.add_car(fiesta)
else:
    print("Your car was not a car!")
"""
