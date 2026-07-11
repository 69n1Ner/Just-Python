from turtle import *
lt(90)
tracer(0)
down()
k=10
for _ in range(2):
    fd(28*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
fd(14*k)
rt(90)
fd(10*k)
lt(90)
down()
for _ in range(2):
    fd(30*k)
    rt(90)
    fd(7*k)
    rt(90)
up()
for x in range(-30,30):
    for y in range(-30,30):
        setpos(x*k,y*k)
        dot(2,'red')
done()