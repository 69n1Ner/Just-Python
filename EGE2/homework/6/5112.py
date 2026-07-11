from turtle import *
tracer(0)
lt(90)
down()
k=10
for _ in range(10):
    fd(10*k)
    for _ in range(2):
        fd(10*k)
        rt(90)
up()
for x in range(-30,30):
    for y in range(-30,30):
        setpos(x*k,y*k)
        dot(2,'red')
done()