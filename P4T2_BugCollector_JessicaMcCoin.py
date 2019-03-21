# Description: This program uses a for loop for enter the number of bugs collected
# each day for 9 days and add them together.
# Date: 7 March 2019
# CTI-110 P4T2a: Bug Collector
# Name: Jessica McCoin 
#

# import turtle into program
# set total = 0
# input bugs collected for a day
# add bugs collected to total
# display total

def main():
    
    #Initialize the accumaulator
    total = 0

    #Get the bugs collected for each day
    for day in range(1, 8):
        #prompt the user
        print('Enter the bugs collected on day', day)

        #Input the number of bugs.
        bugs = int(input())

        #Add bugs to total.
        total += bugs

    # Display the total bugs
    print('You collected a total of', total, 'bugs.')
    
main()
