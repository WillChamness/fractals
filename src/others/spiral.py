import turtle

turtle.bgcolor("black")
pen = turtle.Turtle()
pen.speed("fastest")


# not a fractal but looks awesome
def draw_edges(angle, initial_length, cutoff=100):
    length = initial_length
    color = "red"
    for _ in range(cutoff):
        pen.pencolor(color)
        pen.forward(length)
        pen.right(angle)
        length += 1
        color = "blue" if color == "red" else "red"


slow_motion = True
if slow_motion:
    draw_edges(89, 1, 1000)
else:
    turtle.tracer(0, 0)
    draw_edges(89, 1, 1000)
    turtle.update()

turtle.mainloop()