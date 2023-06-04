import turtle

def execute(pen, sentence, invert):
    dist = 3

    for c in sentence:
        if c == "F":
            pen.forward(dist)
        elif c == "+":
            if not invert:
                pen.left(90)
            else:
                pen.right(90)
        elif c == "-":
            if not invert:
                pen.right(90)
            else:
                pen.left(90)


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
    pen = turtle.Turtle()
    pen.speed("fastest")
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)

    pen.penup()
    pen.backward(350)
    pen.left(90)
    pen.forward(25)
    pen.right(90)
    pen.pendown()

    ITERATIONS = 5
    axiom = "F"
    rules = {
        "F": "F+F-F-F+F"
    }
    sentence = create_sentence(axiom, rules, ITERATIONS)

    slow_mode = False
    start = pen.pos()
    if slow_mode:
        execute(pen, sentence, False)
        pen.penup()
        pen.goto(start)
        pen.pendown()
        execute(pen, sentence, True)
    else:
        turtle.tracer(0, 0)
        execute(pen, sentence, False)
        pen.penup()
        pen.goto(start)
        pen.pendown()
        execute(pen, sentence, True)
        turtle.update()

    turtle.mainloop()

if __name__ == "__main__":
    main()