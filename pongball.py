from turtle import Turtle
import random


def random_ball(option):
    if option == -1:
        return random.choice([135,45,315,225])
    elif option == 0:
        return random.choice([45, 315])
    else:
        return random.choice([135,225])


class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        # pos = -1 --> left defender
        self.color("white")
        self.penup()
        self.shape("circle")
        self.setheading(random_ball(-1))
        self.ball_speed = 0.1

    def move(self,ld,rd,sb):
        self.forward(10)
        self.collision(ld,rd,sb)

    def collision(self,ld,rd,sb):
        if self.xcor() <= -400:
            sb.increase_score(1)
            self.goto(0,0)
            self.setheading(random_ball(-1))
            self.ball_speed = 0.1
        elif self.xcor() >= 400:
            sb.increase_score(0)
            self.goto(0,0)
            self.setheading(random_ball(-1))
            self.ball_speed = 0.1
        elif self.ycor() >= 290 or self.ycor() <= -290:
            self.setheading((360 - self.heading()) % 360)
        elif self.near_defender(ld):
            self.setheading(random_ball(0))
            self.ball_speed *= 0.9
        elif self.near_defender(rd):
            self.setheading(random_ball(1))
            self.ball_speed *= 0.9
            #self.setheading((180 - self.heading()) % 360)
        self.forward(20)

    def near_defender(self,defender):
        return self.distance(defender) <= 40


