from turtle import Turtle, Screen

ramu = Turtle()
screen = Screen()
a = 0


def move_forwards():
    ramu.forward(10)


def move_backwards():
    ramu.backward(10)


def rotate_clockwise():
    ramu.left(10)


def rotate_counterclockwise():
    ramu.right(10)


def clear_screen():
    ramu.reset()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=rotate_clockwise)
screen.onkey(key='a', fun=rotate_counterclockwise)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
