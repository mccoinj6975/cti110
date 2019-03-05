# Description: This program is used to calculate the area of two rectangles and provide
# the user with the rectangle with the greater area.
# Date: 19 February 2019
# CTI-110 P3T1_AreasOfRectangles
# Name: Jessica McCoin 
#

# Enter the length and width of rectangle 1.
# Enter the length and width of rectangle 2
# Calculate the area of both rectangles by multiplying length times width.
# Determine which rectangle has a greater area.
# Display which rectangle has the greater area or if they have an equal area.

# Enter the dimensions of rectange 1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# Enter the dimensions of rectange 2.
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

#Calculate the area's of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

#Determine which has the greater area.
if area1 > area2:
    print('Rectangle 1 has the larger area.')
elif area2 > area1:
    print('Rectangle 2 has the larger area.')
else:
    print('Both rectangles have equal area.')
    
