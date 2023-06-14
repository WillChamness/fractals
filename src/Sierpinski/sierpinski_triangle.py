import turtle

def execute(pen, sentence):
    dist = 5
    angle = 120

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
    pen.speed("fastest")
    pen.hideturtle()

    pen.penup()
    pen.goto(-300, 300)
    pen.pendown()

    ITERATIONS = 7
    axiom = "F-G-G"
    rules = {
        "F": "F-G+F+G-F",
        "G": "GG"
    }
    sentence = create_sentence(axiom, rules, ITERATIONS)

    slow_mode = True
    if slow_mode:
        execute(pen, sentence)
    else:
        turtle.tracer(0, 0)
        execute(pen, sentence)
        turtle.update()

    turtle.mainloop()

if __name__ == "__main__":
    main()