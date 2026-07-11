from turtle import *
tracer(0)
lt(90)
down()
k=10
lt(40)
for _ in range(5):
    rt(-95)
    fd(12*k)
    lt(45)
    fd(8*k)
    lt(40)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(2)
done()