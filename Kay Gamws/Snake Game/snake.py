import turtle
import tkinter
import time
import random 
delay=0.2
win = turtle.Screen()
win.title("KAY's Snake Game")
win.bgcolor("#f6d55c")
win.setup(width=600,height=600)
win.tracer(0)

head = turtle.Turtle()
head.speed(0.5)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"


#segments.append(head)
border = turtle.Turtle()
border.hideturtle()
border.pensize(5)
border.color("#537510")
border.penup()
border.goto(-290,-290)
border.pendown()
border.goto(-290,290)
border.goto(290,290)
border.goto(290,-290)
border.goto(-290,-290)
border.penup()



score = 0
high_score = 0   
segments = []


def move():
    if head.direction == "up":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y + 20)
 
    if head.direction == "down":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y - 20)
 
    if head.direction == "right":
        x = head.xcor() #y coordinate of the turtle
        head.setx(x + 20)
 
    if head.direction == "left":
        x = head.xcor() #y coordinate of the turtle
        head.setx(x - 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"


# move the food to a random position on screen
def food_dis():
    if food.distance(head) <15:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        global score
        global high_score

        score = score + 1
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("  Score:{}  High Score:{} ".format(score , high_score), align="center", font=("Comic sans ms", 20, "normal"))

        

def move_head():
    global segments
    for index in range(len(segments)-1, 0, -1):
        new_body = segments[index-1]
        x = new_body.xcor()
        y = new_body.ycor()
        (segments[index]).goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
def colli():
    global score
    global high_score
    global segments
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments = []
        score = 0
        pen.clear()
        pen.write("  Score:{}  High Score:{} ".format(score , high_score), align="center", font=("Comic sans ms", 20, "normal"))

def body_colli():
    global segments
    for i in range(1,len(segments)):
        if segments[i].distance(segments[0]) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments = []
    


#window
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")


# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#ed553b")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#ed553b")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("  Score:{}  High Score:{} ".format(score , high_score), align="center", font=("Comic sans ms", 20, "normal"))



#main game
while True:
    win.update()
    time.sleep(delay)
    food_dis()
    move()
    move_head()
    colli()
    body_colli()
    
    


tkinter.mainloop()
