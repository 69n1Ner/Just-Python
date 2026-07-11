from turtle import *

screensize(3000,3000)
down()
tracer(0)
k=30
for _ in range(5):
    rt(45)
    fd(10*k)
    rt(45)
for _ in range(6):
    fd(20*k)
    rt(90)
up()
for x in range(-20,30):
    for y in range(-20, 30):
        setpos(x*k,y*k)
        dot(2)
done()