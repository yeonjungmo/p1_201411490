import random
item=[1,2,3,4,5,6]
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape("turtle")
t1.color("red")
t1.penup()
t1.goto(-250,0)
t2=turtle.Turtle()
t2.penup()
t2.goto(-275,-20)
t2.pendown()
def Square():
    t2.fd(70)
    t2.left(90)
    t2.fd(70)
    t2.left(90)
    t2.fd(70)
    t2.left(90)
    t2.fd(70)
    t2.left(90)
def S():
    t2.penup()
    t2.goto(-230,15)
    t2.pendown()
    t2.right(180)
    t2.fd(15)
    t2.left(90)
    t2.fd(15)
    t2.left(90)
    t2.fd(15)
    t2.right(90)
    t2.fd(15)
    t2.right(90)
    t2.fd(15)
def E():
    t2.penup()
    t2.goto(240,20)
    t2.pendown()
    t2.fd(15)
    t2.left(90)
    t2.fd(15)
    t2.left(90)
    t2.fd(15)
    t2.back(15)
    t2.right(90)
    t2.fd(15)
    t2.left(90)
    t2.fd(15)
    
for i in range(0,8):
    Square()
    t2.fd(70)
S()
E()

def TurtleGame():
    sel=raw_input("you play the game(y)")
    if(sel == 'y'):
        for i in range(0,1000):
            sal=raw_input("turtle moving(k)")
            if(sal=='k'):
                random.shuffle(item)
                if(item[0]<=3):
                    if(t1.pos()==(-250,0)):
                        print "game over"


                    print "turtle back"
                    t1.back(70)
                if(item[0]>=4):
                    if(t1.pos()==(170,0)):
                        print "game Success good luck"
                        print i+"points"

                    print "turtle go"
                    t1.fd(70)

            i = i+1
            print i
            print t1.pos()
