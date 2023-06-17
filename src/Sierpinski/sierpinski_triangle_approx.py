import turtle
import random


def generate(pen, vertexes, seed, iterations):
    point = seed
    for _ in range(iterations):
        pen.penup()
        pen.goto(point)
        print(point)
        pen.pendown()

        pen.dot(3, "black")
        vertex = vertexes[random.randint(0, 2)]
        midpoint = ((point[0] + vertex[0]) / 2, (point[1] + vertex[1]) / 2)
        point = midpoint


def draw_triangle(pen):
    side_len = 400
    vertexes = []

    # set initial pos
    pen.penup()
    pen.left(90)
    pen.forward(200)
    pen.left(150)
    pen.pendown()

    # draw triangle
    vertexes.append(pen.pos())
    pen.forward(side_len)
    pen.left(120)
    vertexes.append(pen.pos())
    pen.forward(side_len)
    pen.left(120)
    vertexes.append(pen.pos())
    pen.forward(side_len)

    return vertexes



pen = turtle.Turtle()
pen.speed("slowest")
vertexes = draw_triangle(pen)
SEED = (25, 30) # initial starting point
ITERATIONS = 10000

print(vertexes) 
pen.speed("fastest")
slow_mode = False

if slow_mode:
    generate(pen, vertexes, SEED, ITERATIONS)
else:
    turtle.tracer(0, 0)
    generate(pen, vertexes, SEED, ITERATIONS)
    turtle.update()

turtle.mainloop()