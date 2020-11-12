class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def road_calc(self):
        print(self.length * self.width * 25 * 0.05)

test_road = Road(1000, 15)
test_road.road_calc()

