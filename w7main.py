import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape("turtle")
x=dict()
x=({0:(0,0),1:(0,100),2:(100,100),3:(100,0),4:(0,0)})

def drawSquareAtSave(size,pos):
    tracks=list()
    t1.penup()
    t1.setpos(pos,0)
    t1.pendown()
    for i in range(0,4):
        t1.fd(100)
        t1.right(90)
        tracks.append(t1.pos())
    print tracks
def drawSquareFront():
    for j in range(1,5):
        t1.goto(x[j])
        
def lab7_1():
    mytracks=drawSquareAtSave(100,100)
    print mytracks
def lab7_2():
    drawSquareFront()
    
def main():
    lab7_1()
    lab7_2()
    
if __name__=="__main__":
    main()
