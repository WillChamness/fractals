import turtle

def execute(pen, sentence, invert):
    dist = 10

    for c in sentence:
        if c == "A":
            pen.forward(dist)
        elif c == "B":
            pen.penup()
            pen.forward(dist)
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
    pen = turtle.Turtle()
    pen.speed("fastest")
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)

    pen.penup()
    pen.backward(400)
    pen.pendown()

    ITERATIONS = 7
    axiom = "A"
    rules = {
        "A": "ABA",
        "B": "BBB"
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