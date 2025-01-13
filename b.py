import s as turtle
s.speed(0)
s.pensize(2)
s.bgcolor("black")
for a in range(300):
  s.pencolor("red")
  s.rt(a)
  s.circle(300,a)
  s.fd(a)
  s.rt(145)

s.done
