# Description: This program uses a for loop to calculate the number of calories burned on
# a treadmill after 20, 35, and 45 minutes assuming you burn 5 calories per minute.
# Date: 19 March 2019
# CTI-110 P4HW1: Calories Burned
# Name: Jessica McCoin 
#

# create a while loop to range from 19 to 46
# incriment minutes by 1 through the loop
# create if/else statements to select the numbers 20, 35, 45
# print out the calories burned for 20, 35, 45 minutes

def main():
    
    minutes = 19          #set minutes to 19 where the loop will begin
    while minutes < 46:   #begining of while loop
        #print(i)
        minutes += 1      #incriment minutes by 1 to keep the loop going 
        if minutes == 20:
            print('The amount of calories burned for 20 minutes is 100.')
        elif minutes == 35:
            print('The amount of calories burned for 35 minutes is 175.')
        elif minutes == 45:
            print('The amount of calories burned for 45 minutes is 225.')
        else:
            continue    #keep the loop going until it reaches 46
        
    
main()
