class Car:
    id = 1

    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.id = Car.id
        Car.id += 1

    def go(self):
        print(self.name,'is moving')

    def stop(self):
        self.speed = 0
        print(self.name, 'stoped')

    def turn(self, direction):
        print(self.name, 'turned ', direction)

    def show_speed(self):
        print(f'{self.name}`s speed is {self.speed} km/h')

    def acceleration(self, value):
        if self.speed == 0:
            self.go()
            self.speed += value
        else:
            self.speed += value
        self.show_speed()


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name}`s speed is {self.speed} km/h')
        if self.speed > 60:
            print(f'{self.name}`s speed is exceeded by {self.speed - 60} km/h')


class PoliceCar(Car):
    def flashing_lights(self):
        print(f'{self.name}`s flashing lights is on')


class WorkCar(Car):
    def side_door(self):
        print(f'{self.name}`s side door is working')


class SportCar(Car):
    def nitro(self):
        print('attention!')


ford = TownCar('first car', 'green', 35, False)
nissan = TownCar('second car', 'red', 20, False)
audi = SportCar('sport car', 'green', 20, False)
vw = PoliceCar('police car', 'special', 20, True)

ford.go()
nissan.go()
ford.turn('left')
ford.stop()
ford.show_speed()
nissan.show_speed()
ford.acceleration(15)
nissan.turn('right')
ford.acceleration(25)
ford.acceleration(35)
vw.go()
vw.show_speed()
vw.flashing_lights()
audi.go()
audi.acceleration(100)
audi.nitro()





