import sympy as sp 
import turtle
import random


def T1(point):
    matrix = sp.Matrix([[point[0]], [point[1]]])
    result = sp.Matrix([[0, 0], [0, 0.16]]).multiply(matrix) + sp.Matrix([[0], [0]])
    return (result[0], result[1])

def T2(point):
    matrix = sp.Matrix([[point[0]], [point[1]]])
    result = sp.Matrix([[0.85, 0.04], [-0.04, 0.85]]).multiply(matrix) + sp.Matrix([[0], [1.6]])
    return (result[0], result[1])

def T3(point):
    matrix = sp.Matrix([[point[0]], [point[1]]])
    result = sp.Matrix([[0.2, -0.26], [0.23, 0.22]]).multiply(matrix) + sp.Matrix([[0], [1.6]])
    return (result[0], result[1])

def T4(point):
    matrix = sp.Matrix([[point[0]], [point[1]]])
    result = sp.Matrix([[-0.15, 0.28], [0.26, 0.24]]).multiply(matrix) + sp.Matrix([[0], [0.44]])
    return (result[0], result[1])


def generate(pen, seed, iterations):
    point = seed
    for _ in range(iterations):
        pen.penup()
        pen.goto(point[0]*65, 38*point[1]-252)
        pen.pendown()
        pen.dot(2)

        rndm = random.randint(1, 100)
        if rndm == 1:
            point = T1(point)
        elif 2 <= rndm and rndm <= 86:
            point = T2(point)
        elif 87 <= rndm and rndm <= 93:
            point = T3(point)
        elif 94 <= rndm and rndm <= 100:
            point = T4(point)



pen = turtle.Turtle()
pen.speed("fastest")
pen.color("green")

SEED = (0, 0)
ITERATIONS = 40000
slow_mode = False
if slow_mode:
    generate(pen, SEED, ITERATIONS)
else:
    turtle.tracer(0, 0)
    generate(pen, SEED, ITERATIONS)
    turtle.update()

pen.hideturtle()
turtle.mainloop()
