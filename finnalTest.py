import turtle
import random
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape("turtle")
t1.color("blue")
t2=turtle.Turtle()
point=0
item={1,2}
def S():
    t2.fd(150)
    t2.right(90)
    t2.fd(140)
    t2.right(90)
    t2.fd(150)
    t2.right(90)
    t2.fd(140)
    t2.right(90)
def AS():
    for i in range(0,4):
        S()
        t2.fd(150) 
def ASS():
    t2.penup()
    t2.goto(-300,280)
    t2.pendown()
    AS()
    t2.penup()
    t2.goto(-300,140)
    t2.pendown()
    AS()
    t2.penup()
    t2.goto(-300,0)
    t2.pendown()
    AS()
    t2.penup()
    t2.goto(-300,-140)
    t2.pendown()
    AS()
def one():
    t2.right(90)
    t2.fd(40)
    t2.left(90)
def two():
    t2.fd(20)
    t2.right(130)
    t2.fd(30)
    t2.left(130)
    t2.fd(20)
def three():
    t2.fd(20)
    t2.right(90)
    t2.fd(20)
    t2.right(90)
    t2.fd(20)
    t2.back(20)
    t2.left(90)
    t2.fd(20)
    t2.right(90)
    t2.fd(20)
    t2.right(180)
def draw():
    t2.penup()
    t2.goto(-225,210)
    t2.pendown()
    three()
    t2.penup()
    t2.goto(-225,70)
    t2.pendown()
    one()
    t2.penup()
    t2.goto(-225,-70)
    t2.pendown()
    two()
    t2.penup()
    t2.goto(-225,-210)
    t2.pendown()
    three()
    t2.penup()
    t2.goto(-112.5,210)
    t2.pendown()
    two()
    t2.penup()
    t2.goto(-112.5,70)
    t2.pendown()
    two()
    t2.penup()
    t2.goto(-112.5,-70)
    t2.pendown()
    one()
    t2.penup()
    t2.goto(-112.5,-210)
    t2.pendown()
    two()
    t2.penup()
    t2.goto(112.5,210)
    t2.pendown()
    one()
    t2.penup()
    t2.goto(112.5,70)
    t2.pendown()
    two()
    t2.penup()
    t2.goto(112.5,-70)
    t2.pendown()
    three()
    t2.penup()
    t2.goto(112.5,-210)
    t2.pendown()
    two()
    t2.penup()
    t2.goto(225,210)
    t2.pendown()
    three()
    t2.penup()
    t2.goto(225,70)
    t2.pendown()
    one()
    t2.penup()
    t2.goto(225,-70)
    t2.pendown()
    two()
    t2.penup()
    t2.goto(225,-210)
    t2.pendown()
    one()
def TurtleGame():
    sel=raw_input("you play the game(y)")
    if(sel == 'y'):
        for i in range(0,1000):
            sal=raw_input("turtle moving(k)")
            if(sal=='k'):
                random.shuffle(item)
                a=t1.pos()
                if(item[0]==1):
                    print "your moving just one"
                    print "move yout turtle"
                    if((0,0)< a <(-150,140)):
                        point=point+2
                        return point
                    if((0,0)<a <(150,140)):
                        point=point+2
                        return point
                    if((0,0)<a<(-150,140)):
                        point=point+1
                        return point
                    if((0,0)<a<(150,-140)):
                        point=point+3
                        return point
                    else:
                        print"no no please back"
                        
                        
                if(item[0]==2):
                    print "your moving just two"
                    print "move yout turtle"
                    if((0,0)< a <(-150,140)):
                        point=point+2
                    
                        if(item[0]-1>0):
                            if((-150,140)<a<(-300,280)):
                                point=point+3
                                return point
                            if((-300,0)<a<(-150,140)):
                                point=point+1
                                return point
                            if((-300,-140)<a<(-150,0)):
                                point=point+2
                                return point
                            if((-150,-140)<a<(0,0)):
                                point=point+1
                                return point
                            if((0,0)<a<(150,-140)):
                                point=point+3
                                return point
                            if((0,0)<a<(150,140)):
                                point=point+2
                                return point
                            if((0,140)<a<(150,280)):
                                point=point+1
                                return point
                            if((0,140)<a<(-150,280)):
                                point=point+2
                                return point
                            else:
                                print"no no please back"
                            
                        return point      
                    if((0,0)<a <(150,140)):
                        point=point+2
                        
                        if(item[0]-1>0):
                            if((150,140)<a<(300,280)):
                                point=point+3
                                return point
                            if((150,0)<a<(300,140)):
                                point=point+1
                                return point
                            if((150,-140)<a<(300,0)):
                                point=point+2
                                return point
                            if((0,-140)<a<(150,0)):
                                point=point+3
                                return point
                            if((-150,-140)<a<(0,0)):
                                point=point+1
                                return point
                            if((-150,0)<a<(0,140)):
                                point=point+2
                                return point
                            if((-150,140)<a<(0,280)):
                                point=point+2
                                return point
                            if((0,140)<a<(150,280)):
                                point=point+1
                                return point
                            else:
                                print"no no please back"
                        return point
                    if((0,0)<a<(-150,140)):
                        point=point+1
                        if(item[0]-1>0):
                            if((150,0)<a<(300,140)):
                                point=point+1
                                return point
                            if((150,-140)<a<(300,0)):
                                point=point+2
                                return point
                            if((150,-280)<a<(300,-140)):
                                point=point+1
                                return point
                            if((0,-280)<a<(150,-140)):
                                point=point+2
                                return point
                            if((-150,-140)<a<(0,-280)):
                                point=point+2
                                return point
                            if((-150,-140)<a<(0,0)):
                                point=point+1
                                return point
                            if((-150,0)<a<(0,140)):
                                point=point+2
                                return point
                            if((0,0)<a<(150,140)):
                                point=point+2
                                return point
                            else:
                                print"no no please back"
                        return point
                        
                    if((0,0)<a<(150,-140)):
                        point=point+3
                        if(item[0]-1>0):
                            if((0,0)<a<(150,140)):
                                point=point+2
                                return point
                            if((0,-140)<a<(150,0)):
                                point=point+3
                                return point
                            if((0,-280)<a<(150,-140)):
                                point=point+2
                                return point
                            if((-150,-280)<a<(0,-140)):
                                point=point+2
                                return point
                            if((-300,-280)<a<(150,-140)):
                                point=point+3
                                return point
                            if((-300,-140)<a<(-150,0)):
                                point=point+2
                                return point
                            if((-300,0)<a<(-150,140)):
                                point=point+1
                                return point
                            if((-150,0)<a<(0,140)):
                                point=point+2
                                return point
                            else:
                                print"no no please back"
                        return point
                        
                    else:
                        print"no no please back"
                

def keyup():
    t1.forward(45)

def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keydown():
    t1.back(45)

def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye, "q")
def mousegoto(x,y):
    msg="mouse clicked {0} {1}".format(x,y)
    wn.title(msg)
    t1.setpos(x,y)

def addMouse():
    wn.onclick(mousegoto)
def gamePlay():
    addKeys()
    addMouse()
    ASS()
    draw()
    TurtleGame()
    wn.listen()
    turtle.mainloop()

def lab14():
    gamePlay()
