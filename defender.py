from turtle import Turtle
UP = 90
DOWN = 270

class Defender(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.pos = pos
        self.color("white")
        # pos = -1 --> left defender
        self.setheading(UP)
        self.resizemode("user")
        self.shape("square")
        self.shapesize(1,5)
        self.color("white")
        self.penup()
        self.move_speed = 60
        if pos == -1:
            self.goto(-350,0)
        else:
            self.goto(350, 0)

    def move_up(self):
        self.move_forward(UP)

    def move_down(self):
        self.move_forward(DOWN)

    def move(self,pb):
        if pb.heading() < 90 or pb.heading() > 270:
            #TODO mover para o proximo da bola
            ref_point = pb.ycor()
        else:
            #TODO mover para centro
            ref_point = 50

        if abs(abs(self.ycor()) - abs(ref_point)) > 20:
            if self.ycor()>ref_point:
                self.move_forward(DOWN)
            else:
                self.move_forward(UP)

        #
        # if self.heading() == UP:
        #     if self.ycor() <= 260:
        #         self.move_forward(UP)
        #     else:
        #         self.move_forward(DOWN)
        # else:
        #     if self.ycor() >= -260:
        #         self.move_forward(DOWN)
        #     else:
        #         self.move_forward(UP)

    def move_forward(self,heading):
        self.setheading(heading)
        self.forward(self.move_speed)

    def hard(self):
        if self.move_speed <60:
            self.move_speed += 20

    def soft(self):
        if self.move_speed >20:
            self.move_speed -= 20