import turtle 
import time
import random

speed = 0.15

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("lightgreen")
window.setup(width = 600, height = 600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0, 100)
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 0)
food.shapesize(0.80, 0.80)

queues = []
score = 0

text = turtle.Turtle()
text.speed(0)
text.shape('square')
text.color('white')
text.penup()
text.goto(0, 260)
text.hideturtle()
text.write('Score {}'.format(score), align = 'center', font = ('Courier', 24, 'normal'))

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

def goUp():
    if head.direction != 'down':
        head.direction = 'up'

def goDown():
    if head.direction != 'up':
        head.direction = 'down'

def goRight():
    if head.direction != 'left':
        head.direction = 'right'

def goLeft():
    if head.direction != 'right':
        head.direction = 'left'

window.listen()
window.onkey(goUp, 'Up')
window.onkey(goDown, 'Down')
window.onkey(goRight, 'Right')
window.onkey(goLeft, 'Left')

while True:
    window.update()

    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        for tail in queues:
            tail.goto(1000, 1000)
        
        queues = []
        score = 0
        text.clear()
        text.write('Score {}'.format(score), align = 'center', font = ('Courier', 24, 'normal'))
        
        speed = 0.15
    
    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        score = score + 10
        text.clear()
        text.write('Score {}'.format(score), align = 'center', font = ('Courier', 24, 'normal'))

        speed = speed - 0.001

        yenitail = turtle.Turtle()
        yenitail.speed(0)
        yenitail.shape('square')
        yenitail.color('white')
        yenitail.penup()
        queues.append(yenitail)
    
    for i in range(len(queues) -1, 0, -1):
        x = queues[i - 1].xcor()
        y = queues[i - 1].ycor()
        queues[i].goto(x, y)
    
    if len(queues) > 0:
        x = head.xcor()
        y = head.ycor()
        queues[0].goto(x, y)
    
    move()
    time.sleep(speed)