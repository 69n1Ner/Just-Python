from turtle import *
lt(90)
down()
tracer(1)
k=10
for _ in range(4):
    fd(16*k)
    lt(90)
    fd(20*k)
    lt(90)
up()
fd(4*k)
lt(90)
fd(8*k)
rt(180)
down()
for _ in range(3):
    fd(35*k)
    lt(90)
    fd(6*k)
    lt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        setpos(x*k,y*k)
        dot(2,'red')
done()