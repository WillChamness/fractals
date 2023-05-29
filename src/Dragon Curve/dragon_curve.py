import turtle

def execute(pen, sentence):
    dist = 2.5
    angle = 90

    for c in sentence:
        if c == "F" or c == "G":
            pen.forward(dist)
        elif c == "+":
            pen.left(angle)
        elif c == "-":
            pen.right(angle)


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
    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    pen.speed("fastest")
    pen.hideturtle()

    pen.penup()
    pen.left(90)
    pen.forward(150)
    pen.right(90)
    pen.backward(200)
    pen.pendown()

    ITERATIONS = 16
    axiom = "F"
    rules = {
        "F": "F+G",
        "G": "F-G"
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