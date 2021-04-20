class Car():
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'The car {self.name} has started!')
    def stop(self):
        print(f'The car {self.name} has stopped!')
    def turn(self, direction):
        print(f'The car {self.name} has turned in {direction} direction!')
    def show_speed(self):
        print(f'Your speed is {self.speed} kms/hr')
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('You are moving too fast! Slow down!')
        else:
            print(f'Your speed is {self.speed} kms/hr')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('You are moving too fast! Slow down!')
        else:
            print(f'Your speed is {self.speed} kms/hr')
class PoliceCar(Car):
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police
        if self.is_police is False:
            print('Wrong, you are driving a police car!!!')
class SportCar(Car):
    pass

pol_1 = PoliceCar(90, 'blue', 'pol', False)
pol_2 = PoliceCar(90, 'blue', 'pol', True)
sport_1 = SportCar(230, 'black', 'Audi', False)
work_1 = WorkCar(44, 'grey', 'kamaz', False)
work_2 = WorkCar(39, 'grey', 'kamaz', False)
town_1 = TownCar(70, 'red', 'honda', False)
town_2 = TownCar(58, 'white', 'hyundai', False)

sport_1.go()
sport_1.turn('right')
sport_1.show_speed()
sport_1.stop()

pol_2.go()
pol_2.turn('left')
pol_2.show_speed()
pol_2.stop()

work_1.go()
work_1.turn('right')
work_1.show_speed()
work_1.stop()

work_2.go()
work_2.turn('left')
work_2.show_speed()
work_2.stop()

town_1.go()
town_1.turn('right')
town_1.show_speed()
town_1.stop()

town_2.go()
town_2.turn('left')
town_2.show_speed()
town_2.stop()


