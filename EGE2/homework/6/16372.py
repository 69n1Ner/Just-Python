from turtle import *
lt(90)
down()
tracer(0)
k=10
for _ in range(2):
    fd(23*k)
    lt(90)
    bk(27*k)
    lt(90)
up()
bk(5*k)
rt(90)
fd(11*k)
lt(90)
down()
for _ in range(2):
    fd(26*k)
    rt(90)
    fd(32*k)
    rt(90)
up()
for x in range(-30,50):
    for y in range(-30,50):
        setpos(x*k,y*k)
        dot(2,'red')
done()