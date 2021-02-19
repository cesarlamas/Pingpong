import turtle
window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

# Left Paddle
Paddle_L = turtle.Turtle()
Paddle_L.speed(0)
Paddle_L.shape("turtle")
Paddle_L.color("Blue")
Paddle_L.penup()
Paddle_L.goto(-350,0)
Paddle_L.shapesize(stretch_wid=5,stretch_len=1)


# Right Paddle
Paddle_R = turtle.Turtle()
Paddle_R.speed(1000)
Paddle_R.shape("turtle")
Paddle_R.color("Red")
Paddle_R.penup()
Paddle_R.goto(350,0)
Paddle_R.shapesize(stretch_wid=5,stretch_len=1)

#score
score_a = 0
score_b = 0

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.dx = 0.07
Ball.dy = -0.07

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write( "Player A: 0, Player B:0", align="center", font=("courier",24,"normal"))

#moving the paddles

def Paddle_L_Up():
	y = Paddle_L.ycor()
	y = y + 20
	Paddle_L.sety(y)

def Paddle_L_Down():
	y = Paddle_L.ycor()
	y = y -20
	Paddle_L.sety(y)

def Paddle_R_Up():
	y = Paddle_R.ycor()
	y = y + 20
	Paddle_R.sety(y)

def Paddle_R_Down():
	y = Paddle_R.ycor()
	y = y -20
	Paddle_R.sety(y)

#keybord binding

window.listen()
window.onkeypress(Paddle_L_Up, "w")
window.onkeypress(Paddle_L_Down, "s")
window.onkeypress(Paddle_R_Up, "Up")
window.onkeypress(Paddle_R_Down, "Down")




while True:
	window.update()
	newx = Ball.xcor() + Ball.dx
	newy = Ball.ycor() + Ball.dy
	Ball.setx(newx)
	Ball.sety(newy)
	#border check
	if Ball.ycor() > 290:
		Ball.sety(290)
		Ball.dy = Ball.dy * -1
	elif Ball.ycor() < -290:
		Ball.sety(-290)
		Ball.dy = Ball.dy * -1
	if Ball.xcor() > 390:
		score_a += 1
		pen.clear()
		pen.write( "Player A: {}, Player B: {}".format(score_a,score_b), align="center", font=("courier",24,"normal"))
		Ball.goto(0,0)
		Ball.dx = Ball.dx * -1
	elif Ball.xcor() < -390:
		score_b += 1
		pen.clear()
		pen.write( "Player A: {}, Player B: {}".format(score_a,score_b), align="center", font=("courier",24,"normal"))
		Ball.goto(0,0)
		Ball.dx = Ball.dx * -1
	if (-350 < Ball.xcor() < -340) and Ball.ycor() < Paddle_L.ycor() + 50 and Ball.ycor() > Paddle_L.ycor() -50:
		Ball.dx = Ball.dx * -1

	if (350 > Ball.xcor() > 340) and Ball.ycor() < Paddle_R.ycor() + 50 and Ball.ycor() > Paddle_R.ycor() -50:
		Ball.dx = Ball.dx * -1
