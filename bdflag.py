from turtle import *
hideturtle()

#rectangle draw
color('green')
fillcolor('green')
begin_fill()
forward(180)
left(90)
forward(100)
left(90)
forward(180)
left(90)
forward(100)
end_fill()

#circle draw
color('red')
fillcolor('red')
begin_fill()
penup()
goto(70,50)
pendown()
circle(20)
end_fill()


#stick draw
color('black')
penup()
goto(0,100)
pendown()
pensize(10)
forward(300)
