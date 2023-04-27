#CTI 110-P4LAB1a
#Anquandah Augustine
#04/26/2023






import turtle

# create a turtle object
my_turtle = turtle.Turtle()

# draw a square
i = 0
while i < 4:
    my_turtle.forward(100)
    my_turtle.right(90)
    i += 1

# move turtle to a new location
my_turtle.penup()
my_turtle.goto(150, 0)
my_turtle.pendown()

# draw a triangle
i = 0
while i < 3:
    my_turtle.forward(100)
    my_turtle.left(120)
    i += 1

# keep the turtle window open until closed manually
turtle.done()
