# Description: This program is used to calculate students grades by
# recieving a number grade and calculating a letter grade.
# Date: 28 February 2019
# P3TLAB: Debugging
# Name: Jessica McCoin 
#

# Recieve a number grade from the user
# Define the letter grades and there values
# Determine if the the grade is A,B,C,D, or F 
# Print out the letter grade for the number grade given
#

def main():

    #Enter the number grade 
     score = float(input('Enter grade: '))

    # system uses 10-point grading scale from A to D, anything lower being an F
     A_score = 90
     B_score = 80
     C_score = 70
     D_score = 60
     
    #Determine the letter grade for the given number grade and print out the answer
     if A_score <= score:
        print('\nYour grade is: A')
     elif B_score <= score < A_score:
        print('\nYour grade is: B')
     elif C_score <= score < B_score:
        print('\nYour grade is: C')
     elif D_score <= score < C_score:
        print('\nYour grade is: D')
     else:
        print('\nYour grade is: F') 

# program start
main()
