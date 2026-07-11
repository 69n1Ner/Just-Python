from turtle import *

down()
lt(90)
tracer(0)
k=10
for _ in range(3):
    fd(2*k)
    rt(90)
    fd(3*k)
    lt(90)
rt(180)
fd(6*k)
rt(90)
fd(9*k)
up()
bk(3*k)
rt(90)
down()
for _ in range(2):
    fd(1*k)
    rt(90)
    fd(2*k)
    lt(90)
rt(180)
fd(3*k)
rt(90)
fd(4*k)
rt(90)
fd(1*k)

up()
for x in range(-20,50):
    for y in range(-20, 50):
        goto(x*k,y*k)
        dot(2)
done()