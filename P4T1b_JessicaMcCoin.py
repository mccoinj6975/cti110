# Description: This program uses Turtle to draw the initials J and M, by picking up
# the cursor the seperate the two letters
# Date: 7 March 2019
# CTI-110 P4T1b: Initials
# Name: Jessica McCoin 
#

# import turtle into program
# create display options: pen size, pen color, cursor design
# draw first initial J
# create a for loop for J
# draw second initial M
# print out the letters 

import turtle
i = turtle.Turtle() #i = initial


#begining of main program
def main():

    
    win = turtle.Screen()   #Begining of turtle program

    #Display Options
    i.pensize(15)            # increase pensize
    i.pencolor("blue")       # set pencolor
    i.shape("turtle")        # set cursor style
    
    #start writing the letter M
    i.penup()
    i.goto(-100,0)  #setting coordinates in an (x,y) format for the letter J to start 
    i.pendown()

    #writing the J
    i.forward(100)
    i.backward(50)
    i.right(90)
    i.forward(100)
    for j in range (12): #for loop to create the curve on the J
        i.right(12)
        i.forward(9)

    # Start of writing the letter M
    i.penup()
    i.goto(100,0)   #Setting coordinates in an (x,y) format for the letter M to start
    i.pendown()

    #writing the M 
    i.right(216)
    i.forward(145)
    i.backward(145)
    i.left(90)
    i.forward(30)
    i.right(75)
    i.forward(153)
    i.left(150)
    i.forward(153)
    i.right(75)
    i.forward(30)
    i.right(90)
    i.forward(145)

    #end commands
    win.mainloop()
    
main()
