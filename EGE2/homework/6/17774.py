from turtle import *
lt(90)
down()
tracer(0)
k=20
for _ in range(5):
    fd(8*k)
    rt(90)
    fd(11*k)
    rt(90)
up()
for x in range(-20,20):
    for y in range(-20, 20):
        setpos(x*k,y*k)
        dot(2,'red')
done()