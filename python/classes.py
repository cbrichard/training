# working with classes

class Car():
    def __init__(self):
        self.color = ''
        print "car started"
    def accel(self,speed):
        print "speeding up to %s mph" % speed
    def turn(self, direction):
        print "turning " + direction
    def stop(self):
        print "stop"

# inheritance

class RaceCar(Car):
    def __init__(self, color):
       self.color = color
       self.top_speed = 200
       print "%s race car started with a top speed of %s" % (self.color, self.top_speed)
    def accel(self, speed):
       print "speeding up to %s mph very very fast" % speed

# create a racecar
race_car = RaceCar('Red')

race_car_variables = vars(race_car)
