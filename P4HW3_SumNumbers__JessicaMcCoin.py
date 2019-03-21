# Description: This program uses a loop to recieve multiple positive numbers and
# display their sum.  The program ends when a negative number is entered.
# Date: 21 March 2019
# CTI-110 P4HW3: Sum of Numbers
# Name: Jessica McCoin 
#

# create a loop that allows the user to enter unlimited positive numbers
# create a criteria that ends the loop once a negative number is entered
# once the loop ends, calculate the sum of all the positive numbers
# display the sum of the positive numbers


#begining of main program
def main():

    #Instructions for user
    print('\n\nEnter positive numbers to find the total')
    print('Enter a negative number to end the program\n')

    pos_num = float(input('Enter number: '))   #first input to start the loop

    total = 0
     
    while pos_num > 0:   #begining of while loop
        if pos_num > 0:
            total += pos_num    #add each positive number to eachother through each loop
            pos_num = float(input('Enter number: '))
    print('\nThe sum of the positive numbers =', format(total, ',.2f'))      #Display the sum of the positive numbers
        

main()
            
