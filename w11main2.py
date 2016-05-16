import turtle
wn=turtle.Screen()
wn.bgpic("C:\Users\P400\Desktop\myMaze.gif")
t1=turtle.Turtle()

t1.shape("turtle")

def keyup():
     t1.fd(50)
 

def keydown():
     t1.back(50)


def keyleft():
     t1.left(90)
  

def keyright():
     t1.right(90)

def addkeys():
     wn.onkey(keyup,"Up")
     wn.onkey(keydown,"Down")
     wn.onkey(keyleft,"Left")
     wn.onkey(keyright,"Right")


addkeys()
wn.listen()
turtle.mainloop()
