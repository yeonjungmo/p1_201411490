import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def keyup():
    t1.forward(100)
def keydown():
    t1.back(100)
def keyleft():
    t1.left(90)
def keyright():
    t1.right(90)

def mousegoto(x,y):
     t1.setpos(x,y)
     

def mouseclcl(x,y):
     if((0<=x<=100)and(y==0)):
           print "check"
def mousesese(x,y):
     if((x==0)and(0<=y<=100)):
           print "check"
   

def keyquit():
     wn.bye()


def addKeys():
     wn.onkey(keyup,"Up")
     wn.onkey(keydown,"Down")
     wn.onkey(keyleft,"Left")
     wn.onkey(keyright,"Right") 
     wn.onkey(keyquit,"q")

def addMouse():
     wn.onclick(mousegoto)
     wn.onclick(mouseclcl)
     wn.onclick(mousesese)
    
def lab11():
     addKeys()
     addMouse()
     wn.listen()
     turtle.mainloop()

lab11()
