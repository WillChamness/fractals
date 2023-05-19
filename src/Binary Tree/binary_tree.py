import turtle

def draw_branch(forward_dist, angle, cutoff=5):
    if cutoff <= 0:
        pen.dot(7)
        return

    # draw branch
    pen.color(0, 255 // cutoff, 0)
    pen.forward(forward_dist)
    # draw left subtree
    pen.left(angle)
    draw_branch(forward_dist*0.8, angle, cutoff-1)
    pen.color(0, 255 // cutoff, 0)
    pen.right(angle)
    # draw right subtree
    pen.right(angle)
    draw_branch(forward_dist*0.8, angle, cutoff-1)
    pen.color(0, 255 // cutoff, 0)
    pen.left(angle)

    # descend back down the tree 
    pen.backward(forward_dist)



pen = turtle.Turtle()
pen.speed("fastest")

pen.left(90)
pen.penup()
pen.backward(150)
pen.pendown()
turtle.colormode(255)

slow_motion = False
iterations = 15
if slow_motion:
    draw_branch(100, 30, iterations)
    pen.hideturtle()
else:
    turtle.tracer(0, 0)
    draw_branch(100, 30, iterations)
    pen.hideturtle()
    turtle.update()


turtle.mainloop()


