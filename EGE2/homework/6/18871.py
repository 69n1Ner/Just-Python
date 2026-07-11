from turtle import *
tracer(0)
lt(90)
down()
k=10
for _ in range(2):
    fd(10*k)
    rt(90)
    fd(20*k)
    rt(90)
up()
bk(4*k)
rt(90)
fd(7*k)
lt(90)
down()
for _ in range(4):
    fd(8*k)
    lt(90)
    fd(12*k)
    lt(90)
up()
fd(10*k)
down()
for _ in range(4):
    fd(12*k)
    rt(90)
up()
for x in range(-40,40):
    for y in range(-40,40):
        setpos(x*k,y*k)
        dot(2,'red')
done()