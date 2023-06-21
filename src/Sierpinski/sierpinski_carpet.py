import turtle

def execute(pen, sentence):
    dist = 3
    angle = 90
    pos_stack = []
    angle_stack = []

    for c in sentence:
        if c == "F":
            pen.forward(dist)
        elif c == "+":
            pen.right(90)
        elif c == "[":
            pos_stack.append(pen.pos())
            angle_stack.append(pen.heading())
        elif c == "]":
            pen.penup()
            pen.setpos(pos_stack.pop())
            pen.setheading(angle_stack.pop())
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
    pen.goto(-400, 400)
    pen.pendown()
    pen.hideturtle()

    ITERATIONS = 5
    axiom = "F"
    rules = {
        "F": "FFF[+FFF+FFF+FFF]"
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