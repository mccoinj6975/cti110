# Description: This program uses Turtle to draw a nested loop, to create a snowflake.
# Date: 20 March 2019
# CTI-110 BONUS LAB: P4T1c: Snowflake
# Name: Jessica McCoin 
#

# import turtle into program
# create display options: pen size, pen color, cursor design
# create a loop for the outer edge of snowflake
# move the cursor to center of outer snowflake
# create another loop for the inside of the snowflake
# print out the snowflake

import turtle
import random
s = turtle.Turtle() #s = shape

s.shape("turtle")

#begining of main program
def main():

    win = turtle.Screen()

    #setup turtle screen    
    win.bgcolor("light blue")
    s.pencolor("white")
    s.speed(9)

    win = turtle.Screen()

    #loop for outer edge of snowflake
    for r in range(8):
        s.left(50)
        for t in range(1):
            s.forward(60)
            s.backward(20)
            s.right(50)
            s.left(20)
            s.forward(20)
            s.backward(20)
            s.right(40)
            s.forward(20)
            s.backward(20)
            s.left(65)

    #move cursor to center of outer edge of snowflake
    s.penup()
    s.goto(-13,22)
    s.pendown()

    #loop for the inner part of the snowflake
    for u in range(8):
        s.left(45)
        for t in range(1):
            s.forward(20)
            s.right(55)
            s.forward(25)
            s.backward(25)
            s.left(55)

        

    win.mainloop()  #end of the turtle program

main()

