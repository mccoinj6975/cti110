# Description: This program is used to display 100 through 300 pounds and their
# equivelant weight in kilograms.  The display is in a table format.
# Date: 21 March 2019
# CTI-110 P4HW2: Pounds to Kilograms
# Name: Jessica McCoin 
#

# create a loop to continue from 100lbs to 300lbs in incriments of 10
# implement the formula kg=lb/2.2046 to convert the pounds to kilograms
# print the answers in a table format
# display the table


#begining of main program
def main():

    print('Pounds \tKilograms')     #begining of table
    print('-----------------')

    lbs = 100          
    while lbs <= 300:       #begining of while loop
        
        kg = lbs/2.2046     #convert lbs to kilograms
        print(format(lbs, ',.2f'), '\t', format(kg, ',.2f'))    #display the pounds and kilograms
        lbs += 10           #inciment each loop by 10 until it reaches 300
        
#end of main program
main()
