import turtle

t = turtle.Turtle()

def draw_square(x, y):

    size = 100
    for _ in range(4):
        t.forward(size)
        t.right(90)

t.onclick(draw_square)

turtle.done()