# Description: This program uses Turtle to draw a square and a triangle
# Date: 7 March 2019
# CTI-110 P4T1a: Shapes
# Name: Jessica McCoin 
#

# import turtle into program
# create while loop to continue from triangle to rectangle
# draw triangle
# draw rectangle
# print out the shapes


import turtle
s = turtle.Turtle()    # s is raplacing turtle in turtle.Turtle()
                       # s = shape


s.shape("turtle")    #Set the cursor in the turtle window to a turtle 

#Enter main program
def main():

    win = turtle.Screen()    #Enter the turtle screen 
    s.left(180)              #Turn the cursor 180 degrees left
    for t in (1,2,3):        #start the for loop t(triangle) for the triangle
        s.forward(120)
        s.left(120)
    for r in (1,2,3,5):      #start the for loop r(rectangle) for the rectangle
        s.forward(120)
        s.right(90)

    
    win.mainloop()           #end of the turtle main loop  
    

#end of main program 
main()
