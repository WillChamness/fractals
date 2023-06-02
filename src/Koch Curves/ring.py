import turtle

def execute(pen, sentence):
    dist = 1

    for c in sentence:
        if c == "F":
            pen.forward(dist)
        elif c == "+":
            pen.left(90)
        elif c == "-":
            pen.right(90)


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
    pen.forward(500)
    pen.left(90)
    pen.forward(200)
    pen.pendown()

    ITERATIONS = 6
    axiom = "F"
    rules = {
        "F": "FF+F+F+F+F+F-F"
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