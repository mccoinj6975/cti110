# Description: This program is used to recieve a projected amount of total sales
# from the user and then displays the profit that will be made from that amount.
# Date: 05 February 2019
# CTI-110 P2T1 - Sales Prediction
# Name: Jessica McCoin 
#

# Get the projected sales.
total_sales = float( input('Enter the projected sales: '))

# Calculate the profit as 23 percent of the total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
 

 
 
