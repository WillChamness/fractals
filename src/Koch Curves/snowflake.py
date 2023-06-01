import turtle

def draw_edge(dist, angle, cutoff=3):
    if cutoff <= 0:
        pen.forward(dist)
        return

    draw_edge(dist / 3, angle, cutoff-1)
    pen.left(angle)
    draw_edge(dist / 3, angle, cutoff-1)
    pen.right(2*angle)
    draw_edge(dist / 3, angle, cutoff-1)
    pen.left(angle)
    draw_edge(dist / 3, angle, cutoff-1)
    

def create_snowflake(sides, edge_length):
    for _ in range(sides):
        draw_edge(edge_length, 60, sides)
        pen.right(360 / sides)


turtle.bgcolor("black")
pen = turtle.Turtle()
pen.speed("fastest")
pen.color("white")
pen.penup()
pen.backward(180)
pen.left(90)
pen.forward(240)
pen.right(90)
pen.pendown()

slow_mode = True
iterations = 5
if slow_mode:
    create_snowflake(iterations, 240)
else:
    turtle.tracer(0, 0)
    create_snowflake(iterations, 240)
    turtle.update()

pen.hideturtle()
turtle.mainloop()