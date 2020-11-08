import time

class TrafficLight:
    def __init__(self):
        self.__color = 'red'

    def running(self):
        while True:
            print(self.__color)
            time.sleep(7)
            self.__color = 'yellow'
            print(self.__color)
            time.sleep(2)
            self.__color = 'green'
            print(self.__color)
            time.sleep(1)
            self.__color = 'red'

tl = TrafficLight()
tl.running()