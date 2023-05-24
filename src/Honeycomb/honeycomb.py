import turtle

def execute(pen, sentence):
    dist = 50
    angle = 60

    for c in sentence:
        if c == "A":
            pen.left(angle)
            pen.forward(dist)
        elif c == "B":
            pen.right(angle)
            pen.forward(dist)


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
    pen.color("black")
    pen.speed("fastest")

    pen.penup()
    pen.right(90)
    pen.forward(300)
    pen.left(90)
    pen.backward(50)
    pen.pendown()

    ITERATIONS = 28
    axiom = "A"
    rules = {
        "A": "AB",
        "B": "A"
    }
    sentence = create_sentence(axiom, rules, ITERATIONS)

    slow_mode = False
    if slow_mode:
        turtle.bgcolor("gold")
        execute(pen, sentence)
    else:
        turtle.tracer(0, 0)
        execute(pen, sentence)
        turtle.bgcolor("gold")
        turtle.update()

    turtle.mainloop()

if __name__ == "__main__":
    main()