import turtle 


def main():
    turtle.bgcolor("black")
    t = turtle.Turtle()
    colors = ["red", "dark red"]
    for number in range(400):
        t.forward(number+1)
        t.right(89)
        t.pencolor(colors[number%2])


if __name__ == "__main__":
    main()
