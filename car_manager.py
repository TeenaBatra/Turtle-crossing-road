from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.new_car = None
        self.all_cars = []
        self.create_car()
        self.move_car()
        self.speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chances = random.randint(1, 6)
        if random_chances == 1:
            self.new_car = Turtle("square")
            self.new_car.penup()
            self.new_car.shapesize(stretch_len=2, stretch_wid=1)
            self.new_car.color(random.choice(COLORS))
            y_pos = random.randint(-240, 255)
            self.new_car.goto(x=300, y=y_pos)
            self.all_cars.append(self.new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed+=MOVE_INCREMENT


