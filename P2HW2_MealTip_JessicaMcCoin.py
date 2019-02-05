# Description: This program is used to recieve an amount from the user for the total
# cost of their meal and recieve how much their tip will cost at 15%, 18%, and 20%.
# Date: 05 February 2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Name: Jessica McCoin 
#

# Get the total cost of meal.
meal_cost = float( input('Enter the cost of your meal: '))

# Calculate the the cost of the customers tip at 15%, 18%, and 20%.
percent_15 = meal_cost * 0.15
percent_18 = meal_cost * 0.18
percent_20 = meal_cost * 0.20

# Calculate the total cost of the customers meal at 15%, 18%, and 20%.
total_15 = percent_15 + meal_cost
total_18 = percent_18 + meal_cost
total_20 = percent_20 + meal_cost

# Display the cost of each tip and the total cost of the meal with the tip.
print('\n15% Tip = $', format(percent_15, ',.2f'), '\tTotal cost of meal = $', format(total_15, ',.2f'))
print('\n18% Tip = $', format(percent_18, ',.2f'), '\tTotal cost of meal = $', format(total_18, ',.2f'))
print('\n20% Tip = $', format(percent_20, ',.2f'), '\tTotal cost of meal = $', format(total_20, ',.2f'))
