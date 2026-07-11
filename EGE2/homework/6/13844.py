from turtle import *
lt(90)
tracer(0)
screensize(4000,4000)
k=100
up()
for _ in range(10):
    rt(120)
    fd(12*k)
down()
for _ in range(7):
    fd(7*k)
    rt(90)
for _ in range(5):
    rt(60)
    fd(20*k)
    rt(30)
up()
for x in range(-30,30):
    for y in range(-30,30):
        setpos(x*k,y*k)
        dot(3,'red')
done()