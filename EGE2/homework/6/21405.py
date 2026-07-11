#6
from turtle import *
lt(90)
down()
tracer(0)
rt(30)
k=30
for f in range(3):
    rt(150)
    fd(6*k)
    rt(30)
    fd(12*k)
up()
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*k,y*k)
        dot(2,'red')
done()