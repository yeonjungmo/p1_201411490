import turtle
wn=turtle.Screen()
wn.bgpic("C:\Users\P400\Desktop\myMaze.gif")
t1=turtle.Turtle()

t1.shape("turtle")
def namo():
     t1.penup()
     t1.goto(100,100)
     t1.pendown()
     t1.fd(100)
     t1.left(90)
     t1.fd(100)
     t1.left(90)
     t1.fd(100)
     t1.left(90)
     t1.fd(100)
     t1.left(90)
     t1.penup()
     t1.home()
     t1.pendown()
     
coord=[(100,100),(200,200)]
curpos=t1.pos()

def isRectangle(curpos,coord):
     return coord[0][1]<=curpos[1]<=coord[1][1] and coord[0][0] <= curpos[0]<=coord[1][0]
     
     
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
     


def main():
     namo() 
     addkeys()
     isRectangle(curpos,coord)
     wn.listen()
     turtle.mainloop()
