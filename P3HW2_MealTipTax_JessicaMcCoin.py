# Description: This program is used to recieve an amount from the user for the total cost of
# their meal and tip amount. The the program will calculate the tip and sales tax. Last it will
# display each caclulation and display them with the total cost of the meal.
# Date: 21 February 2019
# P3HW2 - Meal, Tip and Tax Calculator
# Name: Jessica McCoin 
#

# Enter the charge for the meal.
# Enter the percentage in tip you would like to pay.
# Calculate the tip and the 7 percent sales tax.
# Display the tip, tax, and total cost.

# Get the total cost of meal and the tip the cutomer wants to pay.
meal_cost = float( input('\nEnter the cost of your meal: '))
tip = float( input('Enter the tip percentage: '))

# Calculate the cost of the customers tip.
tip_cost = meal_cost * tip

# Calculate the sales tax for the meal.
sales_tax = meal_cost * 0.07

# Calculate the total cost of the customers meal at 15%, 18%, and 20%.
total = meal_cost + tip_cost + sales_tax

# Display the cost of each tip and the total cost of the meal with the tip.
print('\nTip = $', format(tip_cost, ',.2f'))
print('\nSales Tax = $', format(sales_tax, ',.2f'))
print('\nTotal Cost = $', format(total, ',.2f'))
