import turtle as z
z.bgcolor("black")
z.pensize(2)
z.speed(0)
for i in range(40):
    z.color("green")
    for i in range(4):
        z.circle(40+i*5,-90)
        z.forward(200)
        z.right(90)
    z.left(10)
z.done()