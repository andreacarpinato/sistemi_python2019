#andrea carpinato 
import turtle
import random

num=0
while num<=0:
    num=int(input("Quante braccia vuoi:"))

for i in range(0,num):
    if((random.random()*10)<5):
        turtle.left(90)
        turtle.forward(25)
    else:
        turtle.right(90)
        turtle.forward(25)

turtle.done()