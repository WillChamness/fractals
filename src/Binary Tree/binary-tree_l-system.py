import turtle

def execute(pen, sentence, n):
    pos_stack = []
    angle_stack = []
    dist_stack = []
    dist = 0.075
    angle = 45
    for c in sentence:
        if c == "F":
            pen.forward(dist)
        elif c == "X":
            pen.forward(dist)
            pen.dot(7, "light green") 
        elif c == "L":
            pos_stack.append(pen.pos())
            angle_stack.append(pen.heading())
            pen.left(angle)
        elif c == "R":
            pen.penup()
            pen.setpos(pos_stack.pop())
            pen.setheading(angle_stack.pop())
            pen.right(angle)
            pen.pendown()
        

            

def create_sentence(axiom, rules, iterations):
    sentence = axiom
    for _ in range(iterations):
        new_sentence = ""
        print(sentence) 
        for i in range(len(sentence)):
            if sentence[i] in rules:
                new_sentence += rules[sentence[i]]
            else:
                new_sentence += sentence[i]

        sentence = new_sentence
    
    return sentence


 
def main():
    turtle.bgcolor("white")
    pen = turtle.Turtle()
    pen.color("green")
    pen.speed("fastest")

    pen.penup()
    pen.right(90)
    pen.forward(300)
    pen.left(180)
    pen.pendown()

    ITERATIONS = 13
    axiom = "X"
    rules = {
        "F": "FF", # move forward
        "X": "FLXRX" # move forward, draw left subtree, draw right subtree, and end
    }
    sentence = create_sentence(axiom, rules, ITERATIONS)

    slow_mode = False
    if slow_mode:
        execute(pen, sentence, ITERATIONS)
    else:
        turtle.tracer(0, 0)
        execute(pen, sentence, ITERATIONS)
        turtle.update()
    turtle.mainloop()


if __name__ == "__main__":
    main()



