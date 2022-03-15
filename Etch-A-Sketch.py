from turtle import Turtle, Screen

spot = Turtle()
screen = Screen()


def forward():
    spot.forward(20)


def backward():
    spot.back(20)


def counter_clock():
    spot.left(20)


def clockwise():
    spot.right(20)


def clear_drawing():
    spot.clear()
    spot.reset()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
