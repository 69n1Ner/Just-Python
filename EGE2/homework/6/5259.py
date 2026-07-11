from turtle import *
lt(90)
tracer(0)
down()
color('green')
k=10
fd(80*k)
setpos(0,0)
bk(80*k)
setpos(0,0)
lt(90)
fd(80*k)
setpos(0,0)
bk(80*k)
up()
setpos(10*k,15*k)
down()
color('black')
for _ in range(15):
    for _ in range(20):
        fd(40*k)
        rt(90)
    lt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        setpos(x*k,y*k)
        dot(2,'red')
done()