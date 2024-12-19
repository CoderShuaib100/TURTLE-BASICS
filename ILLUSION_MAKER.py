import turtle

win = turtle.Screen()

win.bgcolor("red")
win.title("ILLUSIONER (TURTLE GRAPHIC)")
win.setup(500,600)
pen = turtle.Turtle()

size = 0
while True:
    for i in range(4):
        pen.fd(size + 1)
        pen.left(90)
        size = size - 5
    size = size + 1

turtle.done()