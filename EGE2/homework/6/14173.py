from turtle import *
tracer(0)
lt(90)
k=10
for _ in range(2):
    down()
    for _ in range(2):
        fd(8*k)
        rt(90)
        fd(8 * k)
        rt(90)
    up()
    fd(6*k)
    rt(90)
    fd(6 * k)
    lt(90)
rt(180)
fd(4*k)
down()
for _ in range(4):
    fd(8*k)
    rt(270)
up()
for x in range(-30,30):
    for y in range(-30,30):
        setpos(x*k,y*k)
        dot(2,'red')
done()
