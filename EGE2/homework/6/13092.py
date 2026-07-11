from turtle import *
lt(90)
down()
tracer(0)
k=20
for _ in range(4):
    fd(12*k)
    rt(90)
for _ in range(5):
    fd(4*k)
    rt(45)
up()
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*k,y*k)
        dot(3,'red')
done()