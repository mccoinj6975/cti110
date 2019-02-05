# Description: This program is used to recieve a weight in pounds from the program
# user and convert it into kilograms. 
# Date: 05 February 2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Name: Jessica McCoin 
#

# Get the weight in pounds.
lb = float( input('Enter a weight in pounds: '))

# Calculate the conversion of weight in pounds into kilograms.
kg = lb/2.2046

# Display the answer in kilograms.
print('\nThe weight in kilograms is', format(kg, ',.2f'))
 
