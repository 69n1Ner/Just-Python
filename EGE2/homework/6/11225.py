from turtle import *
lt(90)
tracer(0)
k=50
rt(60)
down()
screensize(3000,3000)
for _ in range(2):
    forward(7*k)
    rt(120)
rt(300)
fd(7*k)
for _ in range(2):
    rt(60)
    fd(7*k)
    rt(60)
up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k,y*k)
        dot(2,'red')
rt(300)
fd(7*k)
done()