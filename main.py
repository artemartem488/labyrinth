import turtle
from shapely.geometry import LineString

def end(text):
    screen.clear()
    screen.bgcolor('black')
    # len_text = len(text)*10 // 2
    # pen.goto(-len_text,0)
    pen.color('#ff7f00')
    pen.write(text,align='center',font=('Arial',20,'normal')) 
                    
def move_turtle(x,y):
    global end_flag
    x_start = pen.xcor()
    y_start = pen.ycor()
    line_1 = LineString([(x_start,y_start),(x_start+x,y_start+y)])
    for i in walls:
        line_2 = LineString([(i[0],i[1]),(i[2],i[3])])
        if line_1.intersects(line_2):
            return
    pen.goto(x_start+x,y_start+y)

    if pen.xcor() <= 335 and pen.xcor() >= 295 and pen.ycor() <= -295 and  pen.ycor() >= -335:
        end_flag = True
        pen.up()
        pen.goto(0,0)
        pen.down()

        end('You\n   win')
def move_up():
    pen.setheading(90)
    move_turtle(0,10)

def move_left():
    pen.setheading(180)
    move_turtle(-10,0)

def move_right():
    pen.setheading(0)
    move_turtle(10,0)

def move_down():
    pen.setheading(270)
    move_turtle(0,-10)

def wall(pen,x,y,x_2,y_2):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.goto(x_2,y_2)
    

def draw_sqrt(pen,x,y,n,color):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.setheading(0)
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.right(90)
        pen.forward(n)
    pen.end_fill()

screen = turtle.Screen()
screen.screensize(500,500)
screen.title('Лабиринт')
screen.bgcolor("#00ffff")

end_flag = False

pen = turtle.Pen()
pen.color('black')
pen.pensize(10)
pen.hideturtle()
pen.up()
pen.speed(100)
pen.color('grey')

pen.pensize(5)
walls = [(-355,-345,345,-345),(345,-345,345,355),(345,355,-355,355),(-355,355,-355,-345),
         (-295,345,-295,50),(-295,50,-220,50),(-295,20,-130,20),(-130,20,-130,150),
         (-170,50,-170,190),(-170,190,-45,190),(-130,150,-80,150),(-80,80,-80,150),
         (-45,250,-45,80),(-45,80,30,80),(-130,50,100,50),(100,50,100,150),
         (100,110,150,110),(100,110,180,110),(150,80,200,80),(150,40,200,40),
         (200,40,200,80),(120,10,180,10),(120,10,120,-20),
         (-220,50,-220,240),(-220,240,-100,240),(-295,300,-50,300),
         (-45,250,250,250),(30,80,30,200),(30,200,150,200),(150,200,250,200),
         (250,200,250,-170),(250,-170,200,-170),(200,-170,200,10),(120,10,120,-235),
         (120,-235,250,-235),(250,-235,250,-295),(250,-295,-295,-295),(-295,-295,-295,20),
         (122,-295,122,-345),(150,300,-50,300),(100,300,100,352),(250,250,290,250),
         (290,250,290,-200),(290,200,342,200),(-130,17,-130,-150),(-50,45,-50,-200),
         (20,45,20,-220)]
for i in walls:
    wall(pen,i[0],i[1],i[2],i[3]) 


pen.pensize(2)
draw_sqrt(pen,-305,345,40,'red')
draw_sqrt(pen,335,-295,40,'green')

pen.pensize(5)
pen.shape('turtle')
pen.showturtle()
pen.color('green')
pen.up()
pen.goto(-325,325)
pen.down()

screen.listen()

screen.onkey(move_up, "Up") 
screen.onkey(move_left, "Left")  
screen.onkey(move_right,"Right")
screen.onkey(move_down,'Down')

while end_flag == False:
    screen.update()

turtle.done()