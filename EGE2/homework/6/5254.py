from turtle import *
lt(90)
down()
tracer(0)
k=10
for _ in range(95):
    fd(20*k)
    rt(90)
up()
for x in range(-40,40):
    for y in range(-40,40):
        setpos(x*k,y*k)
        dot(2,'red')
done()