from turtle import Turtle
ALIGNMENT = "center"
FONT=("Courier",80,'normal')

class StoryBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_left = -1
        self.score_right = -1
        self.increase_score(-1)

    def increase_score(self,lr):
        if lr == -1:
            self.score_left += 1
            self.score_right += 1
        elif lr == 0:
            self.score_left += 1
        else:
            self.score_right += 1
        self.clear()
        self.goto(-100,200)
        self.write(self.score_left,align=ALIGNMENT, font=FONT)
        self.goto(100,200)
        self.write(self.score_right,align=ALIGNMENT, font=FONT)
        self.goto(200,270)
        if self.screen.bgcolor() == "black":
            self.write("Beginner", align="left", font=("Courier",20,'normal'))
        elif self.screen.bgcolor() == "orange":
            self.write("Hard", align="left", font=("Courier",20,'normal'))
        else:
            self.write("Unbeatable", align="left", font=("Courier",20,'normal'))
        self.draw_center_line()

    def draw_center_line(self):
        self.color("white")
        self.goto(0,300)
        self.setheading(270)
        for i in range(60):
            if i%2==0:
                self.pendown()
            else:
                self.penup()
            self.forward(10)

