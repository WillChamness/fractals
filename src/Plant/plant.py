import turtle

def execute(pen, sentence):
    dist = 1.75
    angle = 22.5
    pos_stack = []
    angle_stack = []

    for c in sentence:
        if c == "F":
            pen.forward(dist)
        elif c == "+":
            pen.right(angle)
        elif c == "-":
            pen.left(angle)
        elif c == "[":
            pos_stack.append(pen.pos())
            angle_stack.append(pen.heading())
        elif c == "]":
            pen.penup()
            pos, heading = pos_stack.pop(), angle_stack.pop()
            pen.setpos(pos)
            pen.setheading(heading)
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
    turtle.bgcolor("black")
    pen = turtle.Turtle()
    pen.color("green")
    pen.speed("fastest")

    pen.penup()
    pen.right(90)
    pen.forward(300)
    pen.left(180)
    pen.pendown()

    ITERATIONS = 7
    axiom = "X"
    rules = {
        "X": "F-[[X]+X]+F[+FX]-X",
        "F": "FF"
    }
    sentence = create_sentence(axiom, rules, ITERATIONS)

    slow_mode = False
    if slow_mode:
        execute(pen, sentence)
    else:
        turtle.tracer(0, 0)
        execute(pen, sentence)
        turtle.update()

    turtle.mainloop()

if __name__ == "__main__":
    main()