# importing the turtle library
import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(400,500)


pen = turtle.Turtle()

for i in range(1,5):
    pen.forward(100)
    pen.right(90)

turtle.done()