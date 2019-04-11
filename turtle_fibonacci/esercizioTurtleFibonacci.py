#python andrea carpinato esercizio 1 turtle_fibonacci

import turtle

n1, n2 = 1, 1
num=0
while num<=0:
    num=int(input("Inserire il numero di bracci della spirale:"))

for i in range(0,num):
    turtle.forward(n2)
    turtle.left(90)
    temp = n1
    n1 = n2
    n2 = n1 + temp

turtle.done


