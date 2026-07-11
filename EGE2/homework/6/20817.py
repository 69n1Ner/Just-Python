from turtle import *
lt(90)
down()
tracer(0)
k=10
screensize(3000,3000)
for i in range(3):
    fd(27*k)
    rt(90)
    fd(12*k)
    rt(90)
up()
fd(4*k)
rt(90)
fd(6*k)
lt(90)
down()

for i in range(4):
    fd(83*k)
    rt(90)
    fd(77*k)
    rt(90)
up()
for x in range(-20,50):
    for y in range(-20, 50):
        goto(x*k,y*k)
        dot(2)
done()

