import turtle as t
t.shape('turtle')
t.speed('fastest')

t.color('gray')
t.pu()
t.goto(-350,-350)
t.pd()
t.begin_fill()
for x in range(4):
    t.forward(700)
    t.left(90)
t.end_fill()

t.color('white')
t.pu()
t.goto(0,-330)
t.pd()
t.begin_fill()
t.circle(330)
t.end_fill()

t.color('orange')
t.pu()
t.goto(0,-320)
t.pd()
t.begin_fill()
t.circle(320)
t.end_fill()

t.color('yellow')
t.pu()
t.goto(0,-30)
t.pd()
t.begin_fill()
t.circle(30)
t.end_fill()

t.color('aqua')
t.pu()
t.goto(-250,50)
t.pd()
t.begin_fill()
t.seth(-20)
for x in range(6):
    t.forward(30)
    t.left(8)
t.end_fill()

t.begin_fill()
t.seth(160)
for x in range(6):
    t.forward(30)
    t.left(8)
t.end_fill()

t.color('black')
t.pu()
t.goto(-250,50)
t.pd()
t.seth(-20)
for x in range(6):
    t.forward(30)
    t.left(8)

t.seth(160)
for x in range(6):
    t.forward(30)
    t.left(8)

t.pu()
t.goto(100,120)
t.pd()
t.begin_fill()
t.circle(50)
t.end_fill()

t.color('mediumblue')
t.pu()
t.goto(105,110)
t.pd()
t.begin_fill()
t.circle(40)
t.end_fill()

t.color('red')
t.pu()
t.goto(100,-150)
t.pd()
t.begin_fill()
t.seth(-90)
for x in range(60):
    t.forward(5)
    t.right(3)
t.end_fill()

t.color('orange')
t.pu()
t.goto(100,-130)
t.pd()
t.begin_fill()
t.seth(-90)
for x in range(60):
    t.forward(5)
    t.right(3)
t.end_fill()

t.mainloop()
