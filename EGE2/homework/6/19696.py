from turtle import *
down()
tracer(0)
lt(90)
k=50
for _ in range(23):
    rt(120)
    fd(4*k)
    rt(60)
    fd(8*k)
up()
for x in range(-20,50):
    for y in range(-20, 50):
        goto(x*k,y*k)
        dot(2)
done()