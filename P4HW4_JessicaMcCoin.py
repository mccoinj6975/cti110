# Description: This program uses Turtle to draw a nested loop, or creating a new shape
# out of a shape copied multiple times.
# Date: 19 March 2019
# CTI-110 P4HW4: Nested Loops
# Name: Jessica McCoin 
#

# import turtle into program
# create display options: pen size, pen color, cursor design
# create a loop for the snowflake
# print out the letters

import turtle
import random
s = turtle.Turtle() #s = shape

s.shape("turtle")

#begining of main program
def main():

    win = turtle.Screen()

    #setup turtle screen    
    win.bgcolor("black")
    s.pencolor("magenta")
    s.speed(9)

    win = turtle.Screen()
    for r in range(8):
        s.left(45)
        for t in range(2):
            s.forward(90)
            s.left(45)
            s.forward(90)
            s.left(135)
    s.penup()
    s.goto(90,0)
    s.pendown()
            
            
    
    win.mainloop()

main()
