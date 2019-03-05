# Description: This program is used to take two primary colors and provide the user
# with the secondary color they make when mixed.
# Date: 21 February 2019
# CTI-110 P3HW1 - Color Mixer
# Name: Jessica McCoin 
#

# Enter a number representing the color.
# Add the entered colors.
# Determine which secondary color is created by comparing numbers.
# Display the secondary color created or if the color/number entered is invalid.

# Red = 1
# Blue = 2
# Yellow = 3
print('\nEnter 1 for Red, 2 for Blue, 3 for Yellow.\n')

# Enter the number for primary 1 color and primary 2 color.
prime_color1 = int(input('Enter your firt number for primary color 1: '))
prime_color2 = int(input('Enter your second number for primary color 2: '))

#Calculate the mixed colors.
secondary_color = prime_color1 + prime_color2


#Determine which has the greater area.
if secondary_color == 3:
    print('\nThe secondary color is purple.')
elif secondary_color == 5:
    print('\nThe secondary color is green.')
elif secondary_color == 4:
    print('\nThe secondary color is orange.')
else:
    print('\nThe color entered is not a primary color.')
    
    
