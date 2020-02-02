import turtle
import time
import winsound

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-380,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(375,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = -0.4

# instruction
up_ins = turtle.Turtle()
up_ins.speed(0)
up_ins.color("white")
up_ins.penup()
up_ins.hideturtle()
up_ins.goto(0, 260)
up_ins.write("W                                       ↑", align='center', font=('Courier', 24, 'normal'))

down_ins = turtle.Turtle()
down_ins.speed(0)
down_ins.color("white")
down_ins.penup()
down_ins.hideturtle()
down_ins.goto(0, -290)
down_ins.write("S                                       ↓", align='center', font=('Courier', 24, 'normal'))

# pen
time.sleep(2)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.clear()

pen.write(
    "Player A: 0     Player B: 0", align='center', font=('Courier', 24, 'normal'))

# function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # boarder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        if (score_b == 5):
            pen.clear()
            wn.bgpic("smile.gif")
            pen.write("-: Player A Win :-", align='center', font=('Courier', 24, 'normal'))
            winsound.PlaySound("On.wav", winsound.SND_ALIAS)
            exit()
        pen.clear()
        pen.write(
            "Player A: {}     Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        if (score_a == 5):
            pen.clear()
            wn.bgpic("smile.gif")
            pen.write("-: Player B Win :-", align='center', font=('Courier', 24, 'normal'))
            winsound.PlaySound("On.wav", winsound.SND_ALIAS)
            exit()
        pen.clear()
        pen.write(
            "Player A: {}     Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))


    # paddle and ball collection
    if (ball.xcor() > 350 and ball.xcor() < 370 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50)):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -350 and ball.xcor() > -370 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50)):
        ball.setx(-340)
        ball.dx *= -1
