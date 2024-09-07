import turtle as t 
import colorsys
t.tracer(3)
h=0.7
t.bgcolor("black")
t.pensize(2)
t.speed(0)
for a in range(120):
    c=colorsys.hsv_to_rgb(h,1,1)
    t.color(c)
    h+=0.004
    t.circle(120-a,90)
    t.lt(90)
    t.lt(20)
    t.circle(120-a,90)
    t.lt(18)
    
t.done()
