#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
score1      = int(input("Enter test score: "))
score2      = int(input("Enter test score: "))
score3      = int(input("Enter test score: "))

#add all 3 inputs from user for total_score
total_score = round(score1+score2+score3)       # initialize the variable for accumulating scores

# calculate average score using total_score/# of inputs
average_score = (total_score / 3)

# format and display the result
print("======================")

#inlcude "Your Scores:" text to user
print("Your Scores:", score1, score2, score3)
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)

print("Bye")


