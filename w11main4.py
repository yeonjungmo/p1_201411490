import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.penup()
t1.setpos(100,100)
t1.pendown()
for i in range(0,2):
	t1.fd(100)
	t1.left(90)
	t1.fd(5)
	t1.left(90)
t1.penup()
t1.setpos(-100,100)
t1.pendown()
t1.right(180)
for i in range(0,2):
	t1.fd(5)
	t1.right(90)
	t1.fd(100)
	t1.right(90)
t1.right(90)
t1.penup()
t1.goto(-100,-100)
oldpos=t1.pos()
line1=[(100,100),(200,105)]
xs=line1[0][0]
xe=line1[1][0]
ys=line1[0][1]
ye=line1[1][1]
def r1():
	t1.fd(10)
	x=float()
	y=float()
	(x,y)=t1.pos()
	if(xs<=x<=xe and ys<=y<=ye or -ye<=x<=-xs and ys<=y<=xe):
		print ("in square")
		t1.write("not")
		t1.goto(oldpos)
def r2():
	t1.back(10)
def r3():
	t1.right(90)
def r4():
	t1.left(90)
wn.onkey(r1,"Up")
wn.onkey(r2,"Down")
wn.onkey(r3,"Right")
wn.onkey(r4,"Left")
def mousetogo(x,y):
	t1.setpos(x,y)
	(x,y)=t1.pos()
	if(xs<=x<=xe and ys<=y<=ye or -ye<=x<=-xs and ys<=y<=xe):
		print (" in square")
		t1.write("not")
		t1.goto(oldpos)

def addMouse():
	wn.onclick(mousetogo)
addMouse()
wn.listen()
turtle.mainloop()
