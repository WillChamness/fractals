import turtle

def remove_middle(pen, left, right, cutoff=5):
    if cutoff <= 0:
        return
    
    # split the line into thirds
    dist = abs(right - left) / 3
    p1 = left + dist
    p2 = p1 + dist
    
    # erase the middle third
    pen.penup()
    pen.goto((p1, 0))
    pen.pendown()
    draw_vertical_line(pen) 
    pen.color("black")
    pen.goto((p2, 0))
    pen.color("white")
    draw_vertical_line(pen)

    # perform the same on the left third and right third
    remove_middle(pen, left, p1, cutoff-1)
    remove_middle(pen, p2, right, cutoff-1)


def draw_vertical_line(pen):
    pen.left(90)
    pen.forward(100)
    pen.backward(200)
    pen.forward(100)
    pen.right(90)

    

turtle.bgcolor("black")
pen = turtle.Turtle()
pen.color("white")
pen.speed(2)

START = (-330, 330)
# draw initial line
pen.penup()
pen.forward(START[1])
pen.pendown()
draw_vertical_line(pen)
pen.goto(START[0], 0)
draw_vertical_line(pen)

pen.speed(5)
remove_middle(pen, START[0], START[1])

pen.hideturtle()
turtle.mainloop()