from  turtle import Screen
from storyboard import StoryBoard
from defender import Defender
from pongball import PongBall
import time

pong_screen = Screen()
pong_screen.setup(width=800, height=600)
pong_screen.bgcolor("black")
pong_screen.title("My Pong Game")
pong_screen.tracer(0)
pong_screen.listen()

story_board = StoryBoard()
left_defender = Defender(-1)
pong_screen.onkey(left_defender.move_up,"Up")
pong_screen.onkey(left_defender.move_down,"Down")
right_defender = Defender(1)
pong_screen.onkey(right_defender.hard,"h")
pong_screen.onkey(right_defender.soft,"s")
right_defender.move_speed = 20
pong_ball = PongBall()
pong_screen.update()

is_game_on = True
while is_game_on:
    if right_defender.move_speed == 20:
        pong_screen.bgcolor("black")
    elif right_defender.move_speed == 40:
        pong_screen.bgcolor("orange")
    else:
        pong_screen.bgcolor("red")
    print(pong_ball.position())
    print(pong_ball.heading())
    pong_ball.move(left_defender,right_defender,story_board)
    right_defender.move(pong_ball)
    pong_screen.update()
    time.sleep(pong_ball.ball_speed)


