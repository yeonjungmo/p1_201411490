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
curpos=(0,0)

def isRectangle(curpos,coord):
     return coord[0][1]<=curpos[1]<=coord[1][1] and coord[0][0] <= curpos[0]<=coord[1][0]
     
def keyup():
     pt=t1.pos()
    
     t1.fd(50)
     
     isRectangle(pt,coord)
 

def keydown():
     pt=t1.pos()

     t1.back(50)
     isRectangle(pt,coord)


def keyleft():
     pt=t1.pos()

     t1.left(90)
     isRectangle(pt,coord)  

def keyright(): 
     pt=t1.pos()

     t1.right(90)
     isRectangle(pt,coord)

def addkeys():
     wn.onkey(keyup,"Up")
     wn.onkey(keydown,"Down")
     wn.onkey(keyleft,"Left")
     wn.onkey(keyright,"Right")


namo() 
addkeys()
wn.listen()
turtle.mainloop()
